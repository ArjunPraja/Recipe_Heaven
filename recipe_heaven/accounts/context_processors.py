from .models import user_image

def user_profile_image(request):
    if request.user.is_authenticated:
        try:
            user_profile = user_image.objects.get(user=request.user)
            # Return the URL of the profile image
            return {'profile_image_url': user_profile.user_image.url if user_profile.user_image else None}
        except user_image.DoesNotExist:
            return {'profile_image_url': None}
    return {'profile_image_url': None}
