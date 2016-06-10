from rest_framework import viewsets
from rest_framework import permissions


from provider import filters
from provider import models
from provider.permissions import IsProviderOrReadOnly
from serializers import PolygonSerializer, ProviderSerializer


class ProviderViewSets(viewsets.ModelViewSet):
    """provider view sets"""

    permissions = [permissions.IsAdminUser]
    queryset = models.Provider.objects.all()
    serializer_class = ProviderSerializer


class PolygonViewSets(viewsets.ModelViewSet):
    """polygon view sets"""

    permissions = [IsProviderOrReadOnly]
    queryset = models.Polygon.objects.all()
    serializer_class = PolygonSerializer
    filter_class = filters.PolygonFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.provider)
