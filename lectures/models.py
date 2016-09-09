from django.db import models
from django.urls import reverse


class Lecture(models.Model):
    day = models.DateField(unique=True)
    lecture = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('lecture_detail', kwargs={'lecture_id': self.pk})

    def __str__(self):
        return str(self.lecture)

    class Meta:
        ordering = ['-day']
