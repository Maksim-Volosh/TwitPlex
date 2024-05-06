from django.shortcuts import render

from django.http import JsonResponse
from .models import Tweets

def like_tweet(request):
    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        if tweet_id:
            try:
                tweet = Tweets.objects.get(pk=tweet_id)
                user = request.user
                if user in tweet.likes.all():
                    tweet.likes.remove(user)
                else:
                    tweet.likes.add(user)
                likes_count = tweet.likes.count()
                return JsonResponse(likes_count, safe=False)
            except Tweets.DoesNotExist:
                pass
    return JsonResponse({})

def add_to_favorites_tweet(request):
    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        if tweet_id:
            try:
                tweet = Tweets.objects.get(pk=tweet_id)
                user = request.user
                if user in tweet.favorites.all():
                    tweet.favorites.remove(user)
                else:
                    tweet.favorites.add(user)
                favorites_count = tweet.favorites.count()
                return JsonResponse(favorites_count, safe=False)
            except Tweets.DoesNotExist:
                pass
    return JsonResponse({})

