from django.contrib import admin
from django.urls import include, path

from welcome.views import index

app_name = 'welcome'

urlpatterns = [
    path('', index, name="index"),
]
