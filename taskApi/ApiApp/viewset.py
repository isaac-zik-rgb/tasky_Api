from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializers
from .permissions import UserOwnerOrGetAndPostOnly

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = (UserOwnerOrGetAndPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializers