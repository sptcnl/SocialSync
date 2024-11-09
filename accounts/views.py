from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import SignupForm

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupForm