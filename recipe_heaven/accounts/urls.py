from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, user_login, register, user_logout, user_profile, user_upload_images

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),  # Fixed syntax by adding `name='profile'`
    path('upload_user_image/',user_upload_images , name='upload_user_image')  # Fixed syntax by adding `name='profile'`
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
