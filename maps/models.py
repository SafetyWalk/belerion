from django.db import models

class Coordinate(models.Model):
    lat = models.DecimalField(max_digits=35, decimal_places=30)
    lng = models.DecimalField(max_digits=35, decimal_places=30)

    def __str__(self):
        return f"{self.lat}, {self.lng}"

class Polygon(models.Model):
    coordinates = models.ManyToManyField(Coordinate)

    def __str__(self):
        return f"Polygon {self.pk}"
