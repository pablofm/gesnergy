from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from billing.models import Measure


class MeasuresView(ListView):

    model = Measure

    def get_context_data(self, **kwargs):
        context = super(MeasuresView, self).get_context_data(**kwargs)
        context['measures'] = Measure.objects.all()
        return context


class MeasureView(DetailView):
    model = Measure
    pk_url_kwarg = 'measure_id'

    def get_context_data(self, **kwargs):
        context = super(MeasureView, self).get_context_data(**kwargs)
        context['measures'] = Measure.objects.all()
        return context
