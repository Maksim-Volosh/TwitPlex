from django.contrib import admin
from django.urls import include, path

from main.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
]
