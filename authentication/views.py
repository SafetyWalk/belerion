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
    GoogleUserLoginSerializer
)

class ManualUserAPIView(generics.ListAPIView):
    serializer_class = ManualUserSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def post(self, request, *args, **kwargs):
        serializer = ManualUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GoogleUserAPIView(generics.ListAPIView):
    serializer_class = GoogleUserSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
        serializer = GoogleUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
                return Response({"message": "Login success", "data": user_data})
        return Response({"message": "Invalid email or password."})

class GoogleUserLoginAPIView(generics.ListAPIView):
    serializer_class = GoogleUserLoginSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
        serializer = GoogleUserLoginSerializer(data=request.data)
        print(serializer.data)
        if serializer.is_valid():
            # check if user exists
            # if user exists, return user
            # if user does not exist, create user and return user
            if GoogleUser.objects.filter(email=serializer.data['email']).exists():
                return Response(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)