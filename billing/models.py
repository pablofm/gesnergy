from django.db import models


class Measure(models.Model):
    day = models.DateField()
    measure = models.FloatField()


class Pricing(models.Model):
    day = models.DateField()
    price = models.FloatField()
