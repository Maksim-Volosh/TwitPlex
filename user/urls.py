from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from user.views import *

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
    path('edit/', editprofile, name='edit'),
    
    path('<slug:username>/', profile, name='profile'),
    path('get_tweets/<slug:username>/<slug:post_type>/', show_tweets, name='show_tweets'),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)