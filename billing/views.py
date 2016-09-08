from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView


from billing.models import Lecture, Pricing
from billing.tables import LectureTable, PricingTable

from datetime import date, timedelta as td
import random
from django.db import transaction
from django_tables2 import RequestConfig
from django.urls import reverse_lazy


def load_data(self):
    with transaction.atomic():
        january = date(2016, 1, 1)
        today = date.today()
        delta = today - january
        lecture = 0
        for i in range(delta.days + 1):
            lecture += random.randint(1, 25)
            day = january + td(days=i)
            Pricing.objects.create(day=day, price=random.uniform(0, 1))
            Lecture.objects.create(day=day, lecture=lecture)

    return HttpResponseRedirect('/')


def clean_data(self):
    Pricing.objects.all().delete()
    Lecture.objects.all().delete()
    return HttpResponseRedirect('/')


class BillingView(TemplateView):
    template_name = "billing/billing.html"


class LectureListView(ListView):
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super(LectureListView, self).get_context_data(**kwargs)
        lectures = Lecture.objects.all()
        table = LectureTable(lectures)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        context['lectures_list'] = lectures
        return context


class LectureCreateView(CreateView):
    model = Lecture
    fields = '__all__'


class LectureView(DetailView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'


class LectureDeleteView(DeleteView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'
    success_url = reverse_lazy('lecture_list')


class LectureUpdateView(UpdateView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'
    fields = '__all__'
    template_name_suffix = '_update_form'


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
