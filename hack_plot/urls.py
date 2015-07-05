from django.conf.urls import patterns, include, url

from .views import HackPlotHomeView


hackplot_urls = patterns('',
    url(
        r'^$',
        HackPlotHomeView.as_view(),
        name='list'
    ),
    # url(
    #     r'bandwidth/(?P<pk>[0-9]+)/$',
    #     BandwidthTestDetail.as_view(),
    #     name='retrieveupdatedestroy'
    # ),
)

urlpatterns = patterns('',
    url(r'^', include(hackplot_urls, namespace='hackplot')),
)
