from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from lectures.models import Lecture
from pricing.models import Pricing

from datetime import date, timedelta as td
import random
from django.db import transaction


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

    def get_context_data(self, **kwargs):
        context = super(BillingView, self).get_context_data(**kwargs)
        context['total_pricings'] = Pricing.objects.count()
        context['total_lectures'] = Lecture.objects.count()
        context['last_price'] = Pricing.objects.last()
        context['last_lecture'] = Lecture.objects.last()
        return context