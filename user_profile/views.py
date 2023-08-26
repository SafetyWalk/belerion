from rest_framework.response import Response
from rest_framework import generics
from authentication.models import (
    ManualUser,
    GoogleUser
)
from user_profile.serializers import ( 
    ManualUserProfileSerializer,
    GoogleUserProfileSerializer,
    ManualUserEditProfileSerializer
)

class ManualUserProfileAPIView(generics.ListAPIView):
    serializer_class = ManualUserProfileSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def post(self, request, *args, **kwargs):
        serializer = ManualUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if ManualUser.objects.filter(email=serializer.data['email'], password=serializer.data['password']).exists():
                user = ManualUser.objects.get(email=serializer.data['email'], password=serializer.data['password'])
                user_data = {
                    "id": user.id,
                    "email": user.email,
                    "password": user.password,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "mobile_number": user.mobile_number,
                    "photo_url": user.photo_url
                }
                return Response({
                    "message": "Get profile success", 
                    "status": "SUCCESS",
                    "data": user_data
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })

class GoogleUserProfileAPIView(generics.ListAPIView):
    serializer_class = GoogleUserProfileSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
        serializer = GoogleUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if GoogleUser.objects.filter(email=serializer.data['email'], google_uid=serializer.data['google_uid']).exists():
                user = GoogleUser.objects.get(email=serializer.data['email'], google_uid=serializer.data['google_uid'])
                user_data = {
                    "id": user.id,
                    "email": user.email,
                    "google_uid": user.google_uid,
                    "name": user.name,
                    "mobile_number": user.mobile_number,
                    "photo_url": user.photo_url
                }
                return Response({
                    "message": "Get profile success", 
                    "status": "SUCCESS",
                    "data": user_data
                })
        return Response({
            "message": "Invalid email or google uid",
            "status": "FAILED"
        })

class ManualUserEditProfileAPIView(generics.ListAPIView):
    serializer_class = ManualUserProfileSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def put(self, request, *args, **kwargs):
        serializer = ManualUserEditProfileSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if ManualUser.objects.filter(email=serializer.data['email'], password=serializer.data['password']).exists():
                user = ManualUser.objects.get(email=serializer.data['email'], password=serializer.data['password'])
                user.first_name = serializer.data['first_name']
                user.last_name = serializer.data['last_name']
                user.mobile_number = serializer.data['mobile_number']
                user.photo_url = serializer.data['photo_url']
                user.save()
                user_data = {
                    "id": user.id,
                    "email": user.email,
                    "password": user.password,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "mobile_number": user.mobile_number,
                    "photo_url": user.photo_url
                }
                return Response({
                    "message": "Edit profile success", 
                    "status": "SUCCESS",
                    "data": user_data
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })