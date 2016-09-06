from django.conf.urls import url
from billing.views import BillingView, MeasureListView, MeasureView, PricingListView, PricingView

urlpatterns = [
    url(r'^$', BillingView.as_view(), name='billing'),
    url(r'^measures/$', MeasureListView.as_view(), name='measure_list'),
    url(r'^measures/(?P<measure_id>[0-9]+)/$', MeasureView.as_view(), name='measure_detail'),
    url(r'^pricing/$', PricingListView.as_view(), name='pricing_list'),
    url(r'^pricing/(?P<pricing_id>[0-9]+)/$', PricingView.as_view(), name='pricing_detail'),
]
