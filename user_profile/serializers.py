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