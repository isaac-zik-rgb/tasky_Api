from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class GenerateImagePath(object):
    def __int__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/account/{instance.user.id}/images"
        name = f"profile_image.{ext}"
        
        return os.path.join(path, name)
    

profile_image_path = GenerateImagePath

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=profile_image_path, null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username}'s profile"