from typing import Any
from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateImagePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"medial/houses/{instance.id}/images"
        name = f'main.{ext}'
        return os.path.join(path, name) 

# Create your models here.

houseimagePath = GenerateImagePath()

class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120 )
    image = models.ImageField(upload_to=houseimagePath, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    manager = models.OneToOneField('ApiApp.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_house')
    points = models.IntegerField(default=0)
    completed_task_count = models.IntegerField(default=0)
    notcompleted_task_count = models.IntegerField(default=0) 

