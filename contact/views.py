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
                            "email": contact.contact_email,
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
                            "email": contact.contact_email,
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

class ManualUserCreateContactAPIView(generics.ListAPIView):
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
                # create new contact
                contact = Contact.objects.create(
                    manualuser=user,
                    name=request.data['name'],
                    contact_email=request.data['contact_email'],
                    mobile_number=request.data['mobile_number'],
                    photo_url=request.data['photo_url']
                )
                contact.save()
                # add contact to user
                user.contacts.add(contact)
                return Response({
                    "message": "Create contact success", 
                    "status": "SUCCESS",
                    "data": {
                        "id": contact.id,
                        "name": contact.name,
                        "email": contact.contact_email,
                        "mobile_number": contact.mobile_number,
                        "photo_url": contact.photo_url
                    }
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })

class GoogleUserCreateContactAPIView(generics.ListAPIView):
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
                # create new contact
                contact = Contact.objects.create(
                    googleuser=user,
                    name=request.data['name'],
                    contact_email=request.data['contact_email'],
                    mobile_number=request.data['mobile_number'],
                    photo_url=request.data['photo_url']
                )
                contact.save()
                # add contact to user
                user.contacts.add(contact)
                return Response({
                    "message": "Create contact success", 
                    "status": "SUCCESS",
                    "data": {
                        "id": contact.id,
                        "name": contact.name,
                        "email": contact.contact_email,
                        "mobile_number": contact.mobile_number,
                        "photo_url": contact.photo_url
                    }
                })
        return Response({
            "message": "Invalid email or google uid",
            "status": "FAILED"
        })

class ManualUserContactEditAPIView(generics.ListAPIView):
    serializer_class = ManualUserContactSerializer

    def get_queryset(self):
        manual_users = ManualUser.objects.all()
        return manual_users

    def put(self, request, *args, **kwargs):
        serializer = ManualUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if ManualUser.objects.filter(email=serializer.data['email'], password=serializer.data['password']).exists():
                user = ManualUser.objects.get(email=serializer.data['email'], password=serializer.data['password'])
                # check if contact exists
                if Contact.objects.filter(id=request.data['contact_id']).exists():
                    contact = Contact.objects.get(id=request.data['contact_id'])
                    if contact in user.contacts.all():
                        # update contact
                        contact.name = request.data['name']
                        contact.contact_email = request.data['contact_email']
                        contact.mobile_number = request.data['mobile_number']
                        contact.photo_url = request.data['photo_url']
                        contact.save()
                        return Response({
                            "message": "Edit contact success", 
                            "status": "SUCCESS",
                            "data": {
                                "id": contact.id,
                                "name": contact.name,
                                "email": contact.contact_email,
                                "mobile_number": contact.mobile_number,
                                "photo_url": contact.photo_url
                            }
                        })
                return Response({
                    "message": "Contact does not belong to user",
                    "status": "FAILED"
                })
        return Response({
            "message": "Invalid email or password",
            "status": "FAILED"
        })

class GoogleUserContactEditAPIView(generics.ListAPIView):
    serializer_class = GoogleUserContactSerializer

    def get_queryset(self):
        google_users = GoogleUser.objects.all()
        return google_users

    def put(self, request, *args, **kwargs):
        serializer = GoogleUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # check if user exists
            if GoogleUser.objects.filter(email=serializer.data['email'], google_uid=serializer.data['google_uid']).exists():
                user = GoogleUser.objects.get(email=serializer.data['email'], google_uid=serializer.data['google_uid'])
                # check if contact exists
                if Contact.objects.filter(id=request.data['contact_id']).exists():
                    contact = Contact.objects.get(id=request.data['contact_id'])
                    # update contact
                    contact.name = request.data['name']
                    contact.contact_email = request.data['contact_email']
                    contact.mobile_number = request.data['mobile_number']
                    contact.photo_url = request.data['photo_url']
                    contact.save()
                    return Response({
                        "message": "Edit contact success", 
                        "status": "SUCCESS",
                        "data": {
                            "id": contact.id,
                            "name": contact.name,
                            "email": contact.contact_email,
                            "mobile_number": contact.mobile_number,
                            "photo_url": contact.photo_url
                        }
                    })
        return Response({
            "message": "Invalid email or google uid",
            "status": "FAILED"
        })