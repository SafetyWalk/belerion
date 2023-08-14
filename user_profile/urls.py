from django.urls import path
from user_profile.views import (
    ManualUserProfileAPIView,
    GoogleUserProfileAPIView,
)

app_name = 'user_profile'

urlpatterns = [
    path('manual-user/', ManualUserProfileAPIView.as_view(), name='path_manual_user'),
    path('google-user/', GoogleUserProfileAPIView.as_view(), name='path_google_user'),
]