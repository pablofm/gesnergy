from django.test import TestCase
from datetime import date, timedelta as td
from django.core.urlresolvers import reverse
from lectures.models import Lecture


class LectureListTest(TestCase):
    def setUp(self):
        self.measure1 = Lecture.objects.create(day=date.today(), lecture=200)
        self.measure2 = Lecture.objects.create(day=date.today() + td(days=1), lecture=200)
        url = reverse('lecture_list')
        self.response = self.client.get(url)

    def test_measures_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_measures_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'lectures/lecture_list.html')

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
        url = reverse('lecture_detail', kwargs={'lecture_id': self.lecture.id + 1})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_measure_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'lectures/lecture_detail.html')


class LectureCreate(TestCase):
    def setUp(self):
        self.data = {
            'day': '2015-12-21',
            'lecture': 22
        }

    def test_creating_a_lecture_increases_the_number_of_objects(self):
        self.client.post(reverse('lecture_create'), self.data)
        self.assertEqual(1, Lecture.objects.count())

    def test_wrong_data_doestn_work(self):
        self.data['day'] = '2015-2015-2015'
        self.client.post(reverse('lecture_create'), self.data)
        self.assertEqual(0, Lecture.objects.count())


class LectureDelete(TestCase):
    def setUp(self):
        self.lecture = Lecture.objects.create(day=date.today(), lecture=2)

    def test_deleting_a_lecture_decreases_the_number_of_objects(self):
        self.assertEqual(1, Lecture.objects.count())
        self.client.post(reverse('lecture_delete', kwargs={'lecture_id': self.lecture.id}))
        self.assertEqual(0, Lecture.objects.count())

    def test_wrong_data_doestn_work(self):
        self.client.post(reverse('lecture_delete', kwargs={'lecture_id': self.lecture.id+1}))
        self.assertEqual(1, Lecture.objects.count())
