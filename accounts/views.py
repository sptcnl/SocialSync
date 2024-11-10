from rest_framework import generics
from django.contrib.auth import get_user_model, authenticate
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = authenticate(**request.data)

        refresh = RefreshToken.for_user(user)
        return Response({'refresh_token': str(refresh),
                        'access_token': str(refresh.access_token)}, status=status.HTTP_200_OK)