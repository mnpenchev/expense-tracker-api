from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"email": "test@test.com",
                "password": "supersecretpassword",
                "title": "MR",
                "first_name": "First",
                "last_name": "Last"
                }
        response = self.client.post('/auth/register/', data)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
