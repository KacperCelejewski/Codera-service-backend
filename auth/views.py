from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    """
    Rejestracja nowego użytkownika.
    Zwraca token autoryzacyjny po pomyślnej rejestracji.
    """

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data["username"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        logout(request)
        return Response(status=status.HTTP_200_OK, data={"message": "Logged out"})


# Compare this snippet from auth/urls.py:
