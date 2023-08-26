from django.urls import path
from contact.views import (
    ManualUserContactAPIView,
    GoogleUserContactAPIView,
    ManualUserCreateContactAPIView,
    GoogleUserCreateContactAPIView,
    ManualUserContactEditAPIView,
    GoogleUserContactEditAPIView,
    ManualUserContactDeleteAPIView,
    GoogleUserContactDeleteAPIView
)

app_name = 'contact'

urlpatterns = [
    path('manual-user/', ManualUserContactAPIView.as_view(), name='path_manual_user_contact'),
    path('google-user/', GoogleUserContactAPIView.as_view(), name='path_google_user_contact'),
    path('manual-user/create/', ManualUserCreateContactAPIView.as_view(), name='path_manual_user_create_contact'),
    path('google-user/create/', GoogleUserCreateContactAPIView.as_view(), name='path_google_user_create_contact'),
    path('manual-user/edit/', ManualUserContactEditAPIView.as_view(), name='path_manual_user_edit_contact'),
    path('google-user/edit/', GoogleUserContactEditAPIView.as_view(), name='path_google_user_edit_contact'),
    path('manual-user/delete/', ManualUserContactDeleteAPIView.as_view(), name='path_manual_user_delete_contact'),
    path('google-user/delete/', GoogleUserContactDeleteAPIView.as_view(), name='path_google_user_delete_contact')
]