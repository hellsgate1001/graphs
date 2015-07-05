from django.views.generic import TemplateView


class HackPlotHomeView(TemplateView):
    template_name = 'hackplot/hackplot_home.html'
