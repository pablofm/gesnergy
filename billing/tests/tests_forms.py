from django.test import TestCase
from billing.forms import LectureForm, PricingForm


class LectureFormTest(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-12-21',
            'lecture': 215
        }

    def test_form_cant_be_empty(self):
        form = LectureForm({})
        self.assertFalse(form.is_valid())

    def test_day_cant_be_empty(self):
        self.data['day'] = None
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_day_cant_be_wrong(self):
        self.data['day'] = '31/02/2016'
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_lecture_cant_be_empty(self):
        self.data['lecture'] = None
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_lecture_cant_be_negative(self):
        self.data['lecture'] = -20.0
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_correct_form_is_valid(self):
        form = LectureForm(self.data)
        self.assertTrue(form.is_valid())


class PricingFormTest(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-12-21',
            'price': 115.1
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
        self.data['price'] = None
        form = PricingForm(self.data)
        self.assertFalse(form.is_valid())

    def test_correct_form_is_valid(self):
        form = PricingForm(self.data)
        self.assertTrue(form.is_valid())

    def test_lecture_cant_be_negative(self):
        self.data['price'] = -20
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())
