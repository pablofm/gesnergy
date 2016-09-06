from django.test import TestCase
from datetime import date
from django.core.urlresolvers import reverse
from billing.models import Lecture, Pricing


class BillingTest(TestCase):
    def setUp(self):
        url = reverse('billing')
        self.response = self.client.get(url)

    def test_billing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_billing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/billing.html')


class LectureListTest(TestCase):
    def setUp(self):
        self.measure1 = Lecture.objects.create(day=date.today(), lecture=200)
        self.measure2 = Lecture.objects.create(day=date.today(), lecture=200)
        url = reverse('lecture_list')
        self.response = self.client.get(url)

    def test_measures_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_measures_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/lecture_list.html')

    def test_teatros_recibe_la_lista_correcta(self):
        measures = self.response.context['lecture_list']
        self.assertCountEqual(measures, [self.measure1, self.measure2])


class LectureTest(TestCase):
    def setUp(self):
        self.lecture = Lecture.objects.create(day=date.today(), lecture=200)
        url = reverse('lecture_detail', kwargs={'lecture_id': self.lecture.id})
        self.response = self.client.get(url)

    def test_measure_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_measure_that_do_not_exist_implies_404(self):
        lecture = Lecture.objects.create(day=date.today(), lecture=200)
        url = reverse('lecture_detail', kwargs={'lecture_id': lecture.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_measure_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/lecture_detail.html')


class LectureCreate(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-12-21',
            'lecture': 22.15
        }

    def test_creating_a_lecture_increases_the_number_of_objects(self):
        self.client.post(reverse('lecture_create'), self.data)
        self.assertEqual(1, Lecture.objects.count())

    def test_wrong_data_doestn_work(self):
        self.data['day'] = '2015-2015-2015'
        self.client.post(reverse('lecture_create'), self.data)
        self.assertEqual(0, Lecture.objects.count())


class PricingListTest(TestCase):
    def setUp(self):
        self.pricing1 = Pricing.objects.create(day=date.today(), price=22.30)
        self.pricing2 = Pricing.objects.create(day=date.today(), price=42.12)
        url = reverse('pricing_list')
        self.response = self.client.get(url)

    def test_pricing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/pricing_list.html')

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
        pricing = Pricing.objects.create(day=date.today(), price=22.8)
        url = reverse('pricing_detail', kwargs={'pricing_id': pricing.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_pricing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/pricing_detail.html')


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
