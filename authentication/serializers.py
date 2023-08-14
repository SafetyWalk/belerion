from rest_framework import serializers
from authentication.models import (
    ManualUser,
    GoogleUser
)

class ManualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = '__all__'

class GoogleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = '__all__'

class ManualUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['email', 'password']

class GoogleUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['email', 'google_uid']