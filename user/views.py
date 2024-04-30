from datetime import datetime
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.shortcuts import redirect, render
from django.core.cache import cache

from tweet.models import Tweets
from user.forms import LoginForm
from user.models import User

def profile(request, username):
    
    cache_key = f'user_{username}'
    user = cache.get(cache_key)
    
    if not user:
        user: User = User.objects.get(username=username)
        cache.set(cache_key, user, 60)
    
    user_tweets = Tweets.objects.annotate(
        likes_count=Count('likes'),
        favorites_count=Count('favorites')
    ).filter(owner=user).select_related("owner").prefetch_related("likes", "favorites")
        
    tweets_flag = user_tweets.exists()
        
    current_year = datetime.now().year
    
    context = {
        "user": user,
        "tweets": user_tweets,
        "current_year": current_year,
        "tweets_flag": tweets_flag,
    }
    
    return render(request, 'user/profile.html', context)

def show_tweets(request, post_type, username):
    user = User.objects.get(username=username)
    current_year = datetime.now().year
    context = {
        "current_year": current_year,
    }
    
    if post_type == 'tweets': 
        user_tweets = Tweets.objects.annotate(
            likes_count=Count('likes'),
            favorites_count=Count('favorites')
        ).filter(owner=user)
        
        tweets_flag = user_tweets.exists()
        context["tweets"] = user_tweets
        context["tweets_flag"] = tweets_flag
        
    elif post_type == 'favorites':
        favorites_tweets = Tweets.objects.annotate(
            likes_count=Count('likes'),
            favorites_count=Count('favorites')
        ).filter(favorites=user)
        
        tweets_flag = favorites_tweets.exists()
        context["tweets"] = favorites_tweets
        context["tweets_flag"] = tweets_flag
        
    return render(request, 'main/include/tweets.html', context=context)



def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('user:profile', user.username)
    else:
        form = LoginForm()
        
    return render(request, 'user/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('main:index')

