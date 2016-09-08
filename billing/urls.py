from django.conf.urls import url
from billing.views import BillingView
from billing.views import LectureListView, LectureView, LectureCreateView
from billing.views import PricingListView, PricingView, PricingCreateView

from billing.views import clean_data, load_data
urlpatterns = [
    url(r'^$', BillingView.as_view(), name='billing'),
    url(r'^load_data$', load_data, name='load_data'),
    url(r'^clean_data$', clean_data, name='clean_data'),
    # Lectures
    url(r'^lectures/$', LectureListView.as_view(), name='lecture_list'),
    url(r'^lectures/new$', LectureCreateView.as_view(), name='lecture_create'),
    url(r'^lectures/(?P<lecture_id>[0-9]+)/$', LectureView.as_view(), name='lecture_detail'),
    # Pricing
    url(r'^pricing/$', PricingListView.as_view(), name='pricing_list'),
    url(r'^pricing/new$', PricingCreateView.as_view(), name='pricing_create'),
    url(r'^pricing/(?P<pricing_id>[0-9]+)/$', PricingView.as_view(), name='pricing_detail'),
]
