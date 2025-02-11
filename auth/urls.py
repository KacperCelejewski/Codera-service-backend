from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LogoutView

urlpatterns = [
    path("login/", obtain_auth_token, name="api_login"),
    path("register/", RegisterView.as_view(), name="api_register"),
    path("logout/", LogoutView.as_view(), name="api_logout"),
]
