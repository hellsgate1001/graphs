from django.views.generic import ListView

from .models import BandwidthTest


class BandwidthListView(ListView):
    model = BandwidthTest
