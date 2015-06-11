from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Chart, Contact


class HomeView(CreateView):
    model = Contact
    template_name = 'home.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['chart_list'] = Chart.objects.all()
        return context

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        messages.success(self.request, "Thanks for getting in touch, I'll reply to you soon")
        return super(HomeView, self).form_valid(form)
