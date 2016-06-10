from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geomodels
from django.db import models


class Provider(AbstractUser):
    """Provider Data"""

    phone = models.CharField(max_length=10, help_text='10 digit mobile number')
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=225)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Polygon(models.Model):
    """Polygon data"""

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    price = models.FloatField()
    poly = geomodels.PolygonField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
