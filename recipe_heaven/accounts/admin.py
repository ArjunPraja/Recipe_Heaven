from django.contrib import admin
from .models import user_image

@admin.register(user_image)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_image')  # Display fields in the list view
    search_fields = ('user__username',)  # Enable searching by related user
    list_filter = ('user',)  # Filter images by users in the admin panel
