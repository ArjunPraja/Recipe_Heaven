from django.db import models
import uuid

 
    

class user_image(models.Model):
    user_image=models.ImageField(upload_to='user_image/',blank=True, null=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, null=True, blank=True, related_name="user_image"
    )