from django.test import TestCase
from lectures.forms import LectureForm
from lectures.models import Lecture


class LectureFormTest(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-01-01',
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

    def test_lecture_cant_be_smaller_than_another_one(self):
        Lecture.objects.create(day='2015-01-01', lecture=2)
        self.data['lecture'] = 1
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_lecture_cant_be_negative(self):
        self.data['lecture'] = -20.0
        form = LectureForm(self.data)
        self.assertFalse(form.is_valid())

    def test_correct_form_is_valid(self):
        form = LectureForm(self.data)
        self.assertTrue(form.is_valid())
