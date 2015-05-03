from django.views.generic import ListView

from .models import Chart


class HomeView(ListView):
    model = Chart
    template_name = 'home.html'
