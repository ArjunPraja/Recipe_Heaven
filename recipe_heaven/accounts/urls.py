from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from .views import home, user_login, register, user_logout, user_profile, user_upload_images, delete_rating,delete_recipe,remove_favourite

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),  # Fixed syntax by adding `name='profile'`
    path('upload_user_image/',user_upload_images , name='upload_user_image'),
 path('rating_delete/<int:rating_id>', delete_rating, name='delete_rating'),
path('delete_recipe/<int:recipe_id>', delete_recipe, name='delete_recipes'),
path('remove_favourite/<int:favorite_id>/',remove_favourite , name='remove_favourite'),

]
handler404 = 'recipes.views.custom_404'  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
