from django.db import models
from django.urls import reverse


class Pricing(models.Model):
    day = models.DateField(unique=True)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('pricing_detail', kwargs={'pricing_id': self.pk})

    def __str__(self):
        return str(round(self.price, 4))

    class Meta:
        ordering = ['-day']
