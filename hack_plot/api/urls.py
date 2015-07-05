from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import HackIPViewSet, HackLocationViewSet


hackplot_api_urls = patterns('',
    url(
        r'^hack-ip/$',
        HackIPViewSet.as_view({'get': 'list'}),
        name='list_ips'
    ),
    url(
        r'^hack-location/$',
        HackLocationViewSet.as_view({'get': 'list'}),
        name='list_locations'
    ),
)

urlpatterns = patterns('',
    url(r'^', include(hackplot_api_urls, namespace='hackplot_api')),
)
