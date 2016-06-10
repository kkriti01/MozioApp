from rest_framework_gis.serializers import GeoFeatureModelSerializer

from provider import models


class PolygonSerializer(GeoFeatureModelSerializer):
    """polygon serializer"""

    class Meta:
        model = models.Polygon
        geo_field = "poly"
        fields = ['provider', 'name', 'price']
