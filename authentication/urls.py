from django.urls import path
from authentication.views import (
    ManualUserAPIView,
    GoogleUserAPIView,
)

app_name = 'authentication'

urlpatterns = [
    path('manual-user/', ManualUserAPIView.as_view(), name='path_manual_user'),
    path('google-user/', GoogleUserAPIView.as_view(), name='path_google_user'),
]