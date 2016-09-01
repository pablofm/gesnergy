from django.test import TestCase
from datetime import date
from django.core.urlresolvers import reverse
from billing.models import Measure


class BillingListTest(TestCase):
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
        measures = self.response.context['measures']
        self.assertCountEqual(measures, [self.measure1, self.measure2])


class BillingTest(TestCase):
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
