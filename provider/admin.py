from django.contrib.gis import admin

from provider import models

admin.site.register(models.Polygon, admin.GeoModelAdmin)
