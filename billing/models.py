from django.db import models
from django.urls import reverse


class Lecture(models.Model):
    day = models.DateField(unique=True)
    lecture = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('lecture_detail', kwargs={'lecture_id': self.pk})


class Pricing(models.Model):
    day = models.DateField(unique=True)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('pricing_detail', kwargs={'pricing_id': self.pk})
