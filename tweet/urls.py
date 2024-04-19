from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from tweet.views import *

app_name = 'tweet'

urlpatterns = [
    path('like_tweet/', like_tweet, name='like_tweet'),
    path('favorites_tweet/', add_to_favorites_tweet, name='favorites_tweet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)