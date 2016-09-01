from django.conf.urls import url
from billing.views import MeasuresView, MeasureView

urlpatterns = [
    url(r'^measures/$', MeasuresView.as_view(), name='measure_list'),
    url(r'^measures/(?P<measure_id>[0-9]+)/$', MeasureView.as_view(), name='measure_detail'),
]
