from django.test import TestCase
from datetime import date, timedelta as td
from django.core.urlresolvers import reverse
from pricing.models import Pricing


class PricingListTest(TestCase):
    def setUp(self):
        self.pricing1 = Pricing.objects.create(day=date.today(), price=22.30)
        self.pricing2 = Pricing.objects.create(day=date.today() + td(days=1), price=42.12)
        url = reverse('pricing_list')
        self.response = self.client.get(url)

    def test_pricing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'pricing/pricing_list.html')

    def test_pricing_takes_proper_items(self):
        pricing_list = self.response.context['pricing_list']
        self.assertCountEqual(pricing_list, [self.pricing1, self.pricing2])


class PricingTest(TestCase):
    def setUp(self):
        self.pricing = Pricing.objects.create(day=date.today(), price=200.22)
        url = reverse('pricing_detail', kwargs={'pricing_id': self.pricing.id})
        self.response = self.client.get(url)

    def test_pricing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_pricing_that_do_not_exist_implies_404(self):
        url = reverse('pricing_detail', kwargs={'pricing_id': self.pricing.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'pricing/pricing_detail.html')


class PricingCreate(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-12-21',
            'price': 22.15
        }

    def test_creating_a_pricing_increases_the_number_of_objects(self):
        self.client.post(reverse('pricing_create'), self.data)
        self.assertEqual(1, Pricing.objects.count())

    def test_wrong_data_doestn_work(self):
        self.data['day'] = '2015-2015-2015'
        self.client.post(reverse('pricing_create'), self.data)
        self.assertEqual(0, Pricing.objects.count())


class PricingDelete(TestCase):
    def setUp(self):
        self.pricing = Pricing.objects.create(day=date.today(), price=2)

    def test_deleting_a_pricing_decreases_the_number_of_objects(self):
        self.assertEqual(1, Pricing.objects.count())
        self.client.post(reverse('pricing_delete', kwargs={'pricing_id': self.pricing.id}))
        self.assertEqual(0, Pricing.objects.count())

    def test_wrong_data_doestn_work(self):
        self.client.post(reverse('pricing_delete', kwargs={'pricing_id': self.pricing.id+1}))
        self.assertEqual(1, Pricing.objects.count())