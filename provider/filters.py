from rest_framework_gis import filters
from rest_framework_gis.filterset import GeoFilterSet

from provider import models


class PolygonFilter(GeoFilterSet):
    contains_geom = filters.GeometryFilter(name='poly', lookup_type='contains')

    class Meta:
        model = models.Polygon
        fields = ['name', 'price', 'contains_geom']
