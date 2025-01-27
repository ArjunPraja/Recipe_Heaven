from django.contrib import admin
from django.urls import path, include
from .views import recipies, add_recipies
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',recipies,name="recipies"),
    path('add/',add_recipies,name="add_recipies"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
