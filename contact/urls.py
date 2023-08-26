from django.urls import path
from contact.views import (
    ManualUserContactAPIView,
    GoogleUserContactAPIView,
    ManualUserCreateContactAPIView,
    # GoogleUserCreateContactAPIView
)

app_name = 'contact'

urlpatterns = [
    path('manual-user/', ManualUserContactAPIView.as_view(), name='path_manual_user_contact'),
    path('google-user/', GoogleUserContactAPIView.as_view(), name='path_google_user_contact'),
    path('manual-user/create/', ManualUserCreateContactAPIView.as_view(), name='path_manual_user_create_contact'),
    # path('google-user/create/', GoogleUserCreateContactAPIView.as_view(), name='path_google_user_create_contact'),
]