from django.urls import path
from contact.views import (
    ManualUserContactAPIView,
    GoogleUserContactAPIView
)

app_name = 'contact'

urlpatterns = [
    path('manual-user/', ManualUserContactAPIView.as_view(), name='path_manual_user_contact'),
    path('google-user/', GoogleUserContactAPIView.as_view(), name='path_google_user_contact'),
]