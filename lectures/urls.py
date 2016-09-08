from django.conf.urls import url
from lectures.views import LectureListView, LectureView, LectureCreateView, LectureDeleteView, LectureUpdateView

urlpatterns = [
    url(r'^$', LectureListView.as_view(), name='lecture_list'),
    url(r'^new$', LectureCreateView.as_view(), name='lecture_create'),
    url(r'^(?P<lecture_id>[0-9]+)/$', LectureView.as_view(), name='lecture_detail'),
    url(r'^(?P<lecture_id>[0-9]+)/update$', LectureUpdateView.as_view(), name='lecture_update'),
    url(r'^(?P<lecture_id>[0-9]+)/delete$', LectureDeleteView.as_view(), name='lecture_delete'),
]
