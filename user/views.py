from datetime import datetime
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from tweet.models import Tweets
from user.decorators import already_login
from user.forms import LoginForm, ProfileUpdateForm, RegisterForm
from user.models import User


@login_required
def profile(request, username):
        cache_key = f'user_{username}'
        user = cache.get(cache_key)
        
        if not user:
            user = get_object_or_404(User, username=username)
            cache.set(cache_key, user, 60)
        
        user_tweets = Tweets.objects.annotate(
            likes_count=Count('likes', distinct=True),
            favorites_count=Count('favorites', distinct=True)
        ).filter(owner=user).select_related("owner").prefetch_related("likes", "favorites")
            
        tweets_flag = user_tweets.exists()
            
        current_year = datetime.now().year
        
        context = {
            "user": user,
            "tweets": user_tweets,
            "current_year": current_year,
            "tweets_flag": tweets_flag,
            "tweet_type": True
        }
        
        return render(request, 'user/profile.html', context)


@login_required
def editprofile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:profile', request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'user/editprofile.html', {'form': form})


def show_tweets(request, post_type, username):
    user = User.objects.get(username=username)
    current_year = datetime.now().year
    context = {
        "current_year": current_year,
        "tweet_type": False
    }
    
    if post_type == 'tweets': 
        user_tweets = Tweets.objects.annotate(
            likes_count=Count('likes', distinct=True),
            favorites_count=Count('favorites', distinct=True)
        ).filter(owner=user)
        
        tweets_flag = user_tweets.exists()
        context["tweets"] = user_tweets
        context["tweets_flag"] = tweets_flag
        context["tweet_type"] = True
        
    elif post_type == 'favorites':
        favorites_tweets = Tweets.objects.annotate(
            likes_count=Count('likes', distinct=True),
            favorites_count=Count('favorites', distinct=True)
        ).filter(favorites=user)
        
        tweets_flag = favorites_tweets.exists()
        context["tweets"] = favorites_tweets
        context["tweets_flag"] = tweets_flag
        
    return render(request, 'tweets/include/tweets.html', context=context)


@already_login
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            if request.POST.get('next'):
                return HttpResponseRedirect(request.POST.get('next'))
            return redirect('user:profile', user.username)
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@already_login
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return redirect('user:profile', user.username)
    else:
        form = LoginForm()
        
    return render(request, 'user/login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('main:index')

