from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import (BandwidthTestList, BandwidthTestDetail, BandwidthGroupedByDay)


bandwidth_api_urls = patterns('',
    url(
        r'^bandwidth/$',
        BandwidthTestList.as_view(),
        name='listadd'
    ),
    url(
        r'bandwidth/(?P<pk>[0-9]+)/$',
        BandwidthTestDetail.as_view(),
        name='retrieveupdatedestroy'
    ),
    url(
        r'bandwidth/by-day/$',
        BandwidthGroupedByDay.as_view(),
        name='listbyday'
    ),
)

urlpatterns = patterns('',
    url(r'^', include(bandwidth_api_urls, namespace='bandwidth_api')),
)
