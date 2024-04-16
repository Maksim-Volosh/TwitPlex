from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from main.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
