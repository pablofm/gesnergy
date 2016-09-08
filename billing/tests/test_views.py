from django.test import TestCase
from django.core.urlresolvers import reverse


class BillingTest(TestCase):
    def setUp(self):
        url = reverse('billing')
        self.response = self.client.get(url)

    def test_billing_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_billing_call_proper_template(self):
        self.assertTemplateUsed(self.response, 'billing/billing.html')
