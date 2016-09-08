from django.contrib import admin
from lectures.models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ('day', 'lecture')

admin.site.register(Lecture, LectureAdmin)
