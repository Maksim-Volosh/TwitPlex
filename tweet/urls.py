from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from tweet.views import like_tweet

app_name = 'tweet'

urlpatterns = [
    path('', like_tweet, name='like_tweet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)