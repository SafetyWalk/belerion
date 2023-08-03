from rest_framework.response import Response
from rest_framework import generics
from authentication.models import (
    ManualUser,
    GoogleUser
)
from authentication.serializers import ( 
    ManualUserSerializer,
    GoogleUserSerializer
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