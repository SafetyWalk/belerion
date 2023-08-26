from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=20)
    photo_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name