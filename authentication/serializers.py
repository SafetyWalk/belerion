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

class RegisterManualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'mobile_number', 'photo_url']

class RegisterGoogleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['email', 'google_uid', 'name', 'mobile_number', 'photo_url']

class ManualUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['email', 'password']

class GoogleUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['email', 'google_uid']

class ManualUserEditPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualUser
        fields = ['email', 'password']