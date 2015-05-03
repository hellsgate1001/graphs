from django.views.generic import TemplateView, ListView

from .models import BandwidthTest


class BandwidthHomeView(TemplateView):
    template_name = 'bandwidthtest/bandwidthtest_home.html'


class BandwidthListView(ListView):
    model = BandwidthTest
