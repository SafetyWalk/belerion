from rest_framework import serializers
from authentication.models import (
    ManualUser,
    GoogleUser
)

class ManualUserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['contacts']

class GoogleUserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['contacts']