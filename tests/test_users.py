from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import CustomUser

User = get_user_model()


class UsersAPITests(APITestCase):
    def setUp(self):
        client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        response = client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpassword"},
        )
        self.token = response.json()["access"]
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def test_retrieve_own_user_profile(self):
        url = reverse("user-profile", args=[self.user.username])
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_own_user_profile(self):
        url = reverse("user-profile", args=[self.user.username])
        data = {"first_name": "Updated"}
        response = self.client.patch(
            url, data, format="json", HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Updated")

    def test_delete_own_user_profile(self):
        url = reverse("user-profile", args=[self.user.username])
        response = self.client.delete(
            url,
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(username=self.user.username).exists())  # noqa E501

    def test_retrieve_other_user_profile(self):
        other_user = CustomUser.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="otherpassword"
        )
        url = reverse("user-profile", args=[other_user.username])
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
