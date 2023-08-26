from rest_framework import serializers
from authentication.models import (
    ManualUser,
    GoogleUser
)

class ManualUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['email', 'password']

class GoogleUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['email', 'google_uid']

class ManualUserEditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['email', 'password', 'first_name', 'last_name', 'mobile_number', 'photo_url']

class GoogleUserEditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['email', 'google_uid', 'name', 'mobile_number', 'photo_url']