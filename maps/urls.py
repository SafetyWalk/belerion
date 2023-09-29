from django.urls import path
from maps.views import (
    PolygonAPIView
)

app_name = 'maps'

urlpatterns = [
    path('polygon/', PolygonAPIView.as_view(), name='path_maps_polygon'),
]