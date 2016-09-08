from django.contrib import admin
from pricing.models import Pricing


class PricingAdmin(admin.ModelAdmin):
    list_display = ('day', 'price')

admin.site.register(Pricing, PricingAdmin)
