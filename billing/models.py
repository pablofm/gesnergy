from django.db import models


class Lecture(models.Model):
    day = models.DateField()
    lecture = models.FloatField()


class Pricing(models.Model):
    day = models.DateField()
    price = models.FloatField()
