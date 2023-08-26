from rest_framework.response import Response
from rest_framework import generics
from authentication.models import (
    ManualUser,
    GoogleUser
)
from authentication.serializers import ( 
    ManualUserSerializer,
    GoogleUserSerializer,
    ManualUserLoginSerializer,
    GoogleUserLoginSerializer,
    ManualUserEditPasswordSerializer,
    RegisterManualUserSerializer,
    RegisterGoogleUserSerializer,
)

class ManualUserAPIView(generics.ListAPIView):
    serializer_class = ManualUserSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def post(self, request, *args, **kwargs):
        serializer = RegisterManualUserSerializer(data=request.data)
        if serializer.is_valid():
            # check if exists
            if not ManualUser.objects.filter(email=serializer.data['email']).exists():
                serializer.save()
                return Response(serializer.data)
            return Response({
                "message": "User with email already exists",
                "status": "FAILED"
            })
        return Response(serializer.errors)

class GoogleUserAPIView(generics.ListAPIView):
    serializer_class = GoogleUserSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
        serializer = RegisterGoogleUserSerializer(data=request.data)
        if serializer.is_valid():
            # check if exists
            if not GoogleUser.objects.filter(email=serializer.data['email']).exists():
                serializer.save()
                return Response(serializer.data)
            return Response({
                "message": "User with email already exists",
                "status": "FAILED"
            })
        return Response(serializer.errors)

class ManualUserLoginAPIView(generics.ListAPIView):
    serializer_class = ManualUserLoginSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def post(self, request, *args, **kwargs):
        serializer = ManualUserLoginSerializer(data=request.data)
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
                    "message": "Login success", 
                    "status": "SUCCESS",
                    "data": user_data
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })

class GoogleUserLoginAPIView(generics.ListAPIView):
    serializer_class = GoogleUserLoginSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
        serializer = GoogleUserLoginSerializer(data=request.data)
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
                    "message": "Login success", 
                    "status": "SUCCESS",
                    "data": user_data
                })
        return Response({
            "message": "Invalid email or google uid",
            "status": "FAILED"
        })

class ManualUserEditPasswordAPIView(generics.ListAPIView):
    serializer = ManualUserEditPasswordSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users
    
    def put(self, request, *args, **kwargs):
        serializer = ManualUserEditPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if ManualUser.objects.filter(email=serializer.data['email']).exists():
                user = ManualUser.objects.get(email=serializer.data['email'])
                user.password = serializer.data['password']
                user.save()
                return Response({
                    "message": "Password updated successfully",
                    "status": "SUCCESS",
                    "data": {
                        "new_password": serializer.data['password']
                    }
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })