from django.urls import path
from authentication.views import (
    ManualUserAPIView,
    GoogleUserAPIView,
    ManualUserLoginAPIView,
    GoogleUserLoginAPIView,
    ManualUserEditPasswordAPIView
)

app_name = 'authentication'

urlpatterns = [
    path('manual-user/', ManualUserAPIView.as_view(), name='path_manual_user'),
    path('google-user/', GoogleUserAPIView.as_view(), name='path_google_user'),
    path('manual-user/login/', ManualUserLoginAPIView.as_view(), name='path_manual_user_login'),
    path('google-user/login/', GoogleUserLoginAPIView.as_view(), name='path_google_user_login'),
    path('manual-user/edit/password/', ManualUserEditPasswordAPIView.as_view(), name='path_manual_user_edit_password')
]