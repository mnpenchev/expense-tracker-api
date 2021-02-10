from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from ..models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        # self.logout_url = reverse('logout')
        # self.email_verify_url = reverse('email-verify')
        # self.token_refresh_url = reverse('token-refresh')
        # self.request_reset_email_url = reverse('request-reset-email')
        # self.password_reset_confirm_url = reverse('password-reset-confirm')
        # self.password_reset_complete_url = reverse('password-reset-complete')
        self.fake = Faker()

        self.user_data = {
            'email': 'test@test.email',
            'password': self.fake.email(),
            "title": "MR",
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name()
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
