from django.test import TestCase
from billing.forms import MeasureForm, PricingForm


class MeasureFormTest(TestCase):
    def setUp(self):
        self.form = MeasureForm()


class PricingFormTest(TestCase):
    def setUp(self):
        self.form = PricingForm()
