from django.urls import path
from user_profile.views import (
    ManualUserProfileAPIView,
    GoogleUserProfileAPIView,
    ManualUserEditProfileAPIView
)

app_name = 'user_profile'

urlpatterns = [
    path('manual-user/', ManualUserProfileAPIView.as_view(), name='path_manual_user'),
    path('google-user/', GoogleUserProfileAPIView.as_view(), name='path_google_user'),
    path('manual-user/edit/', ManualUserEditProfileAPIView.as_view(), name='path_manual_user_edit'),
]