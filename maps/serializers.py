from rest_framework import serializers
from maps.models import Polygon, Coordinate

class PolygonSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Polygon
        fields = ['id', 'coordinates']

    def get_coordinates(self, obj):
        # Mengambil semua koordinat untuk polygon objek saat ini
        coordinates = obj.coordinates.all()
        
        # Mengubah setiap koordinat menjadi objek {'lat': lat_value, 'lng': lng_value}
        coordinates_data = [{'lat': coord.lat, 'lng': coord.lng} for coord in coordinates]
        
        return coordinates_data
