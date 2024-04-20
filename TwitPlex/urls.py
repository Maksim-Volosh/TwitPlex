from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    # django urls
    path('admin/', admin.site.urls),
    
    #our urls
    path('welcome/', include('welcome.urls')),
    path('', include('main.urls')),
    path('profile/', include('user.urls')),
    
    # ajax requests urls
    path('ajax/', include('tweet.urls')),
]
