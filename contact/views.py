from rest_framework.response import Response
from rest_framework import generics
from authentication.models import (
    ManualUser,
    GoogleUser
)
from authentication.serializers import ( 
    ManualUserLoginSerializer,
    GoogleUserLoginSerializer,
)
from contact.models import (
    Contact
)
from contact.serializers import ( 
    ManualUserContactSerializer,
    GoogleUserContactSerializer,
)

class ManualUserContactAPIView(generics.ListAPIView):
    serializer_class = ManualUserContactSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def post(self, request, *args, **kwargs):
            serializer = ManualUserLoginSerializer(data=request.data)
            if serializer.is_valid():
                # check if user exists
                if ManualUser.objects.filter(email=serializer.data['email'], password=serializer.data['password']).exists():
                    user = ManualUser.objects.get(email=serializer.data['email'], password=serializer.data['password'])
                    contacts = Contact.objects.filter(manualuser=user)
                    contact_list = []
                    for contact in contacts:
                        contact_list.append({
                            "id": contact.id,
                            "name": contact.name,
                            "email": contact.email,
                            "mobile_number": contact.mobile_number,
                            "photo_url": contact.photo_url
                        })
                    return Response({
                        "message": "Get contact success", 
                        "status": "SUCCESS",
                        "data": contact_list
                    })
            return Response({
                "message": "Invalid email or password",
                "status": "FAILED"
            })

class GoogleUserContactAPIView(generics.ListAPIView):
    serializer_class = GoogleUserContactSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def post(self, request, *args, **kwargs):
            serializer = GoogleUserLoginSerializer(data=request.data)
            if serializer.is_valid():
                # check if user exists
                if GoogleUser.objects.filter(email=serializer.data['email'], google_uid=serializer.data['google_uid']).exists():
                    user = GoogleUser.objects.get(email=serializer.data['email'], google_uid=serializer.data['google_uid'])
                    contacts = Contact.objects.filter(googleuser=user)
                    contact_list = []
                    for contact in contacts:
                        contact_list.append({
                            "id": contact.id,
                            "name": contact.name,
                            "email": contact.email,
                            "mobile_number": contact.mobile_number,
                            "photo_url": contact.photo_url
                        })
                    return Response({
                        "message": "Get contact success", 
                        "status": "SUCCESS",
                        "data": contact_list
                    })
            return Response({
                "message": "Invalid email or google uid",
                "status": "FAILED"
            })