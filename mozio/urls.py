from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from provider import views


router = routers.DefaultRouter()
router.register(r'provider', views.ProviderViewSets)
router.register(r'polygon', views.PolygonViewSets)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
