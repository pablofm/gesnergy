from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView

from django.views.generic.list import ListView

from billing.models import Lecture, Pricing


class BillingView(TemplateView):
    template_name = "billing/billing.html"


class LectureListView(ListView):
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super(LectureListView, self).get_context_data(**kwargs)
        context['lecture_list'] = Lecture.objects.all()
        return context


class LectureCreateView(CreateView):
    model = Lecture
    fields = '__all__'


class LectureView(DetailView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'


class PricingCreateView(CreateView):
    model = Pricing
    fields = '__all__'


class PricingListView(ListView):
    model = Pricing

    def get_context_data(self, **kwargs):
        context = super(PricingListView, self).get_context_data(**kwargs)
        context['pricing_list'] = Pricing.objects.all()
        return context


class PricingView(DetailView):
    model = Pricing
    pk_url_kwarg = 'pricing_id'
