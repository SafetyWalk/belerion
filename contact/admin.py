from django.contrib import admin
from contact.models import ( 
    Contact
)

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    fields = []
    list_display = ['name', 'contact_email', 'mobile_number', 'photo_url']
