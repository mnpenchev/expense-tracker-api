from .test_setup import TestSetUp
from ..models import User
from rest_framework import status


class TestViews(TestSetUp):
    def test_user_cannot_register_without_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user_successfully(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_email_already_registered(self):
        pass
