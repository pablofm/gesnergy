from django.db import models
from django.urls import reverse


class Pricing(models.Model):
    day = models.DateField(unique=True)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('pricing_detail', kwargs={'pricing_id': self.pk})
