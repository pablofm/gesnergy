from django.conf.urls import url

from pricing.views import PricingListView, PricingView, PricingCreateView, PricingDeleteView, PricingUpdateView


urlpatterns = [
    url(r'^$', PricingListView.as_view(), name='pricing_list'),
    url(r'^new$', PricingCreateView.as_view(), name='pricing_create'),
    url(r'^(?P<pricing_id>[0-9]+)/$', PricingView.as_view(), name='pricing_detail'),
    url(r'^(?P<pricing_id>[0-9]+)/update$', PricingUpdateView.as_view(), name='pricing_update'),
    url(r'^(?P<pricing_id>[0-9]+)/delete$', PricingDeleteView.as_view(), name='pricing_delete'),
]
