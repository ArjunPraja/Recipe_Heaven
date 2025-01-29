from django.contrib import admin
from django.urls import path, include
from .views import recipies, add_recipies, submit_review, toggle_favourite
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',recipies,name="recipies"),
    path('add/',add_recipies,name="add_recipies"),
     path('submit_review/<int:recipe_id>/', submit_review, name='submit_review'),
    path('favourite/<int:id>/', toggle_favourite, name='toggle_favourite'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
