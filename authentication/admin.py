from django.contrib import admin
from authentication.models import ( 
    ManualUser,
    GoogleUser
)

@admin.register(ManualUser)
class ManualUser(admin.ModelAdmin):
    fields = []
    list_display = ['username', 'email', 'password', 'first_name', 'last_name', 'mobile_number', 'photo_url']

@admin.register(GoogleUser)
class GoogleUser(admin.ModelAdmin):
    fields = []
    list_display = ['google_uid', 'email', 'name', 'mobile_number', 'photo_url']