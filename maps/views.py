from rest_framework.response import Response
from rest_framework import generics
from maps.models import (
    Polygon
)
from maps.serializers import ( 
    PolygonSerializer,
)

class PolygonAPIView(generics.ListAPIView):
    serializer_class = PolygonSerializer

    def get_queryset(self):
        polygons = Polygon.objects.all()
        return polygons