from django.contrib import admin
from billing.models import Pricing, Lecture


class PricingAdmin(admin.ModelAdmin):
    list_display = ('day', 'price')


class LectureAdmin(admin.ModelAdmin):
    list_display = ('day', 'lecture')

admin.site.register(Pricing, PricingAdmin)
admin.site.register(Lecture, LectureAdmin)
