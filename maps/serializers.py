from rest_framework import serializers
from maps.models import (
    Coordinate,
    Polygon
)

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['lat', 'lng']

class PolygonSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True, read_only=True)

    class Meta:
        model = Polygon
        fields = ['id', 'coordinates']
