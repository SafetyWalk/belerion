from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import (
    ManualUser, 
    GoogleUser
)
from authentication.serializers import (
    RegisterManualUserSerializer
)
class ManualUserAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_manual_user(self):
        user_data = {
            "email": "test@example.com",
            "password": "TestPassword123",
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "mobile_number": "0123456789",
            "photo_url": "https://lh3.googleusercontent.com/a/AAcHTtemk3r5u4n_ydV0VGKpvTguJUy1gvT4I6f2wFKsy5OWgPI=s96-c"
        }

        response = self.client.post('/api/v1/authentication/manual-user/', user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ManualUser.objects.count(), 1)
        expected_response = {
            "email": "test@example.com",
            "password": "TestPassword123",
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "mobile_number": "0123456789",
            "photo_url": "https://lh3.googleusercontent.com/a/AAcHTtemk3r5u4n_ydV0VGKpvTguJUy1gvT4I6f2wFKsy5OWgPI=s96-c"
        }
        self.assertDictEqual(response.data, expected_response)
    
    def test_create_existing_manual_user(self):
        user_data = {
            "email": "test@example.com",
            "password": "TestPassword123",
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "mobile_number": "0123456789",
            "photo_url": "https://lh3.googleusercontent.com/a/AAcHTtemk3r5u4n_ydV0VGKpvTguJUy1gvT4I6f2wFKsy5OWgPI=s96-c"
        }

        response = self.client.post('/api/v1/authentication/manual-user/', user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ManualUser.objects.count(), 1)

        response = self.client.post('/api/v1/authentication/manual-user/', user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ManualUser.objects.count(), 1)
        expected_response = {
            "message": "You already have an account, try loggin in with your email and password",
            "status": "FAILED"
        }
        self.assertDictEqual(response.data, expected_response)
