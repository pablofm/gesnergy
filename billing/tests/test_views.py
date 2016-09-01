from django.test import TestCase
from datetime import date
from django.core.urlresolvers import reverse
from billing.models import Measure, Pricing


class MeasureListTest(TestCase):
    def setUp(self):
        self.measure1 = Measure.objects.create(day=date.today(), measure=200)
        self.measure2 = Measure.objects.create(day=date.today(), measure=200)
        url = reverse('measure_list')
        self.response = self.client.get(url)

    def test_measures_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_measures_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/measure_list.html')

    def test_teatros_recibe_la_lista_correcta(self):
        measures = self.response.context['measure_list']
        self.assertCountEqual(measures, [self.measure1, self.measure2])


class MeasureTest(TestCase):
    def setUp(self):
        self.measure = Measure.objects.create(day=date.today(), measure=200)
        url = reverse('measure_detail', kwargs={'measure_id': self.measure.id})
        self.response = self.client.get(url)

    def test_measure_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_measure_that_do_not_exist_implies_404(self):
        measure = Measure.objects.create(day=date.today(), measure=200)
        url = reverse('measure_detail', kwargs={'measure_id': measure.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_measure_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/measure_detail.html')


class PricingListTest(TestCase):
    def setUp(self):
        self.pricing1 = Pricing.objects.create(day=date.today(), price=200)
        self.pricing2 = Pricing.objects.create(day=date.today(), price=200)
        url = reverse('pricing_list')
        self.response = self.client.get(url)

    def test_pricing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/pricing_list.html')

    def test_prices_takes_proper_items(self):
        pricing_list = self.response.context['pricing_list']
        self.assertCountEqual(pricing_list, [self.pricing1, self.pricing2])


class PriceTest(TestCase):
    def setUp(self):
        self.pricing = Pricing.objects.create(day=date.today(), price=200)
        url = reverse('pricing_detail', kwargs={'pricing_id': self.pricing.id})
        self.response = self.client.get(url)

    def test_pricing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_pricing_that_do_not_exist_implies_404(self):
        pricing = Pricing.objects.create(day=date.today(), price=22.8)
        url = reverse('pricing_detail', kwargs={'pricing_id': pricing.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/pricing_detail.html')
