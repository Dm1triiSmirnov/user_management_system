from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class AuthenticationTests(APITestCase):
    def test_user_registration(self):
        url = reverse("user-register")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "testuser")

    def test_user_registration_with_mismatched_passwords(self):
        url = reverse("user-register")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
            "password2": "mismatchedpassword",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_user_login(self):
        user = CustomUser.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        url = reverse("token_obtain_pair")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_user_login_with_invalid_credentials(self):
        url = reverse("token_obtain_pair")
        data = {
            "username": "invaliduser",
            "password": "invalidpassword",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
