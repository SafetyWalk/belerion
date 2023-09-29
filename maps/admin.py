from django.contrib import admin
from maps.models import ( 
    Coordinate,
    Polygon
)

@admin.register(Coordinate)
class Coordinate(admin.ModelAdmin):
    fields = []
    list_display = ['lat', 'lng']

@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    def coordinates_list(self, obj):
        return ", ".join([f"{coord.lat}, {coord.lng}" for coord in obj.coordinates.all()])
    list_display = ['coordinates_list']