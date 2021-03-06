from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graphs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('bandwidthtest.api.urls')),
    url(r'^api/', include('hack_plot.api.urls')),

    url(r'^bandwidth/', include('bandwidthtest.urls')),
    url(r'^ssh-hack/', include('hack_plot.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
)
