from django.urls import path
from .views import home, user_login, register, user_logout, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile')  # Fixed syntax by adding `name='profile'`
]
