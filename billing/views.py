from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from billing.models import Measure, Pricing


class BillingView(TemplateView):
    template_name = "billing/billing.html"


class MeasureListView(ListView):
    model = Measure

    def get_context_data(self, **kwargs):
        context = super(MeasureListView, self).get_context_data(**kwargs)
        context['measure_list'] = Measure.objects.all()
        return context


class MeasureView(DetailView):
    model = Measure
    pk_url_kwarg = 'measure_id'


class PricingListView(ListView):
    model = Pricing

    def get_context_data(self, **kwargs):
        context = super(PricingListView, self).get_context_data(**kwargs)
        context['pricing_list'] = Pricing.objects.all()
        return context


class PricingView(DetailView):
    model = Pricing
    pk_url_kwarg = 'pricing_id'
