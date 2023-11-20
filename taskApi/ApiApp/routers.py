from rest_framework import routers

from .viewset import UserViewsets

app_name = 'ApiApp'

router = routers.DefaultRouter()
router.register('users', UserViewsets)