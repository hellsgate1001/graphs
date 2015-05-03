from django.conf.urls import patterns, include, url

from .views import BandwidthHomeView


# bandwidth_urls = patterns('',
#     url(r'^$', BandwidthHomeView.as_view(), 'list'),
# )

# urlpatterns = patterns('',
#     url(r'^', include(bandwidth_urls, namespace='bandwidthtest')),
# )




bandwidth_urls = patterns('',
    url(
        r'^$',
        BandwidthHomeView.as_view(),
        name='list'
    ),
    # url(
    #     r'bandwidth/(?P<pk>[0-9]+)/$',
    #     BandwidthTestDetail.as_view(),
    #     name='retrieveupdatedestroy'
    # ),
)

urlpatterns = patterns('',
    url(r'^', include(bandwidth_urls, namespace='bandwidthtest')),
)
