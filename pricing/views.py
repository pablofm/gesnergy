from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from pricing.models import Pricing
from pricing.tables import PricingTable
from django_tables2 import RequestConfig
from django.urls import reverse_lazy


class PricingCreateView(CreateView):
    model = Pricing
    fields = '__all__'


class PricingListView(ListView):
    model = Pricing

    def get_context_data(self, **kwargs):
        context = super(PricingListView, self).get_context_data(**kwargs)
        pricing = Pricing.objects.all()
        table = PricingTable(pricing)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        context['pricing_list'] = pricing
        return context


class PricingView(DetailView):
    model = Pricing
    pk_url_kwarg = 'pricing_id'


class PricingDeleteView(DeleteView):
    model = Pricing
    pk_url_kwarg = 'pricing_id'
    success_url = reverse_lazy('pricing_list')


class PricingUpdateView(UpdateView):
    model = Pricing
    pk_url_kwarg = 'pricing_id'
    fields = '__all__'
    template_name_suffix = '_update_form'
