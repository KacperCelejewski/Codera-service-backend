from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, LogoutView, CustomAuthToken

urlpatterns = [
    path("login/", CustomAuthToken.as_view(), name="api_login"),
    path("register/", RegisterView.as_view(), name="api_register"),
    path("logout/", LogoutView.as_view(), name="api_logout"),
]
