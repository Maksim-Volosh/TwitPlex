from django.contrib import admin
from django.urls import include, path

from TwitPlex import settings



urlpatterns = [
    
    # django urls
    path('admin/', admin.site.urls),
    
    #google oauth
    path('accounts/', include('allauth.urls')),
    
    #our urls
    path('welcome/', include('welcome.urls')),
    path('', include('main.urls')),
    path('profile/', include('user.urls')),
    
    # ajax requests urls
    path('ajax/', include('tweet.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]