from django.conf.urls import url
from billing.views import BillingView, LectureListView, LectureView, PricingListView, PricingView

urlpatterns = [
    url(r'^$', BillingView.as_view(), name='billing'),
    url(r'^lectures/$', LectureListView.as_view(), name='lecture_list'),
    url(r'^lectures/(?P<lecture_id>[0-9]+)/$', LectureView.as_view(), name='lecture_detail'),
    url(r'^pricing/$', PricingListView.as_view(), name='pricing_list'),
    url(r'^pricing/(?P<pricing_id>[0-9]+)/$', PricingView.as_view(), name='pricing_detail'),
]
