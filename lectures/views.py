from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from lectures.models import Lecture
from lectures.tables import LectureTable

from django_tables2 import RequestConfig
from django.urls import reverse_lazy


class LectureListView(ListView):
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super(LectureListView, self).get_context_data(**kwargs)
        lectures = Lecture.objects.all()
        table = LectureTable(lectures)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        context['lectures_list'] = lectures
        return context


class LectureCreateView(CreateView):
    model = Lecture
    fields = '__all__'


class LectureView(DetailView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'


class LectureDeleteView(DeleteView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'
    success_url = reverse_lazy('lecture_list')


class LectureUpdateView(UpdateView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'
    fields = '__all__'
    template_name_suffix = '_update_form'
