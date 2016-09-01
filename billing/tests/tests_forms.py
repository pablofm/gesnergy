from django.test import TestCase
from billing.forms import MeasureForm, PricingForm


class MeasureFormTest(TestCase):
    def setUp(self):
        self.data = {
            'day': '21/12/2015',
            'measure': 22.15
        }

    def test_form_cant_be_empty(self):
        form = MeasureForm({})
        self.assertFalse(form.is_valid())

    def test_day_cant_be_empty(self):
        self.data['day'] = None
        form = MeasureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_day_cant_be_wrong(self):
        self.data['day'] = '31/02/2016'
        form = MeasureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_measure_cant_be_empty(self):
        self.data['measure'] = None
        form = MeasureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_correct_form_is_valid(self):
        form = MeasureForm(self.data)
        self.assertTrue(form.is_valid())


class PricingFormTest(TestCase):
    def setUp(self):
        self.data = {
            'day': '21/12/2015',
            'pricing': 115
        }

    def test_form_cant_be_empty(self):
        form = PricingForm({})
        self.assertFalse(form.is_valid())

    def test_day_cant_be_empty(self):
        self.data['day'] = None
        form = PricingForm(self.data)
        self.assertFalse(form.is_valid())

    def test_day_cant_be_wrong(self):
        self.data['day'] = '31/02/2016'
        form = PricingForm(self.data)
        self.assertFalse(form.is_valid())

    def test_measure_cant_be_empty(self):
        self.data['measure'] = None
        form = PricingForm(self.data)
        self.assertFalse(form.is_valid())

    def test_correct_form_is_valid(self):
        form = PricingForm(self.data)
        self.assertTrue(form.is_valid())
