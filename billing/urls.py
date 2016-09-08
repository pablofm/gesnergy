from django.conf.urls import url
from billing.views import BillingView, clean_data, load_data

urlpatterns = [
    url(r'^$', BillingView.as_view(), name='billing'),
    url(r'^load_data$', load_data, name='load_data'),
    url(r'^clean_data$', clean_data, name='clean_data'),
]
