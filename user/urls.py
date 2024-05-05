from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from user.views import *

app_name = 'user'

urlpatterns = [
    path('login/user', login, name='login'),
    path('register/user', register, name='register'),
    path('logout/user', logout, name='logout'),
    
    path('edit/user', editprofile, name='edit'),
    
    path('<slug:username>/', profile, name='profile'),
    path('get_tweets/<slug:username>/<slug:post_type>/', show_tweets, name='show_tweets'),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)