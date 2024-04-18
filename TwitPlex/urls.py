from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', include('welcome.urls')),
    path('', include('main.urls')),
    path('like_tweet/', include('tweet.urls')),
]
