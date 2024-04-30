from datetime import datetime
from django.db.models import Count
from django.shortcuts import render
from django.core.cache import cache

from tweet.models import Tweets
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
        "tweets_flag": tweets_flag,
    }
    
    if post_type == 'tweets': 
        user_tweets = Tweets.objects.annotate(
            likes_count=Count('likes'),
            favorites_count=Count('favorites')
        ).filter(owner=user)
        
        tweets_flag = user_tweets.exists()
        context["tweets"] = user_tweets
        
    elif post_type == 'favorites':
        favorites_tweets = Tweets.objects.annotate(
            likes_count=Count('likes'),
            favorites_count=Count('favorites')
        ).filter(favorites=user)
        
        tweets_flag = favorites_tweets.exists()
        context["tweets"] = favorites_tweets
        
    return render(request, 'main/include/tweets.html', context=context)


