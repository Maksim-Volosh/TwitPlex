from django import template
from django.db.models import Count
from django.http import request
from django.utils.http import urlencode

from tweet.models import Tweets


register = template.Library()

@register.simple_tag
def check_liked_tweets(tweet, user):
    clas = "fi-rs-heart"
    if user.is_authenticated:
        try:
            if tweet.likes.filter(pk=user.pk).exists():
                clas = "fi-ss-heart"
            return clas
        except Tweets.DoesNotExist:
            return clas
    else:
        return clas
    
@register.simple_tag
def check_favorited_tweets(tweet, user):
    clas = "fi-rr-bookmark"
    if user.is_authenticated:
        try:
            if tweet.favorites.filter(pk=user.pk).exists():
                clas = "fi-sr-bookmark"
            return clas
        except Tweets.DoesNotExist:
            return clas
    else:
        return clas