import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestAuthAPI:
    def setup_method(self):
        """Configure the APIClient and URLs for the tests"""
        self.client = APIClient()
        self.register_url = "/auth/register/"
        self.login_url = "/auth/login/"
        self.logout_url = "/auth/logout/"

    def test_register_user(self):
        """Test successful user registration"""
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        response = self.client.post(self.register_url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert "token" in response.data
        assert User.objects.filter(username="testuser").exists()
        assert Token.objects.filter(user__username="testuser").exists()

    def test_register_existing_user(self):
        """Test registering an existing user"""
        User.objects.create_user(username="testuser", password="testpassword")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        response = self.client.post(self.register_url, data, format="json")
        assert (
            response.status_code == status.HTTP_400_BAD_REQUEST
        )  # Powinien zwrócić błąd

    def test_login_user(self):
        """Test user login with correct credentials"""
        user = User.objects.create_user(username="testuser", password="testpassword")
        data = {"username": "testuser", "password": "testpassword"}

        response = self.client.post(self.login_url, data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "token" in response.data
        assert Token.objects.filter(user=user).exists()

    def test_login_invalid_credentials(self):
        """Test logging in with invalid credentials"""
        User.objects.create_user(username="testuser", password="testpassword")
        data = {"username": "testuser", "password": "wrongpassword"}

        response = self.client.post(self.login_url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "token" not in response.data

    def test_logout_user(self):
        """Test user logout"""
        user = User.objects.create_user(username="testuser", password="testpassword")
        token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = self.client.post(self.logout_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Logged out"
        assert not Token.objects.filter(
            user=user
        ).exists()  # Sprawdza, czy token został usunięty

    def test_logout_without_authentication(self):
        """Test logging out without authentication"""
        response = self.client.post(self.logout_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
