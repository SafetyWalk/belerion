from django.db import models

class ManualUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=500)

    def __str__(self):
        return self.email

    @classmethod
    def get_default_pk(cls):
        user, created = cls.objects.get_or_create(
            username='eugeniusms', 
            defaults=dict(
                email='eugeniusms@gmail.com',
                password='Tes123Tes',
                first_name='Eugenius',
                last_name='Mario', 
                mobile_number='0123456789',
                photo_url = 'https://lh3.googleusercontent.com/a/AAcHTtemk3r5u4n_ydV0VGKpvTguJUy1gvT4I6f2wFKsy5OWgPI=s96-c'
            ),
        )
        return user.pk

class GoogleUser(models.Model):
    google_uid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    @classmethod
    def get_default_pk(cls):
        user, created = cls.objects.get_or_create(
            google_uid='1', 
            defaults=dict(
                email='eugeniusms@gmail.com', 
                name='Eugenius Mario', 
                mobile_number='0123456789',
                photo_url='https://lh3.googleusercontent.com/a/AAcHTtemk3r5u4n_ydV0VGKpvTguJUy1gvT4I6f2wFKsy5OWgPI=s96-c'
            ),
        )
        return user.pk