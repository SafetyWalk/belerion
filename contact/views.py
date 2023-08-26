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
    ManualUserEditPasswordSerializer
)
from contact.models import (
    Contact
)
from contact.serializers import ( 
    ManualUserContactSerializer,
    GoogleUserContactSerializer,
)

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