from django.contrib import admin

# Register your models here.
from billing.models import *

admin.site.register(Pricing)
admin.site.register(Lecture)
