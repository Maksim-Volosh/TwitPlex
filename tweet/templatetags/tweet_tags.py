from django import template
from django.db.models import Count
from django.http import request
from django.utils.http import urlencode

from tweet.models import Tweets


register = template.Library()

@register.simple_tag
def check_liked_tweets(twid, user):
    clas = "fi-rs-heart"
    if user.is_authenticated:
        try:
            tweet = Tweets.objects.get(pk=twid)
            if tweet.likes.filter(pk=user.pk).exists():
                clas = "fi-ss-heart"
            return clas
        except Tweets.DoesNotExist:
            return clas
    else:
        return clas