import django_tables2 as tables
from billing.models import Pricing, Lecture


class PricingTable(tables.Table):
    class Meta:
        model = Pricing


class LectureTable(tables.Table):
    class Meta:
        model = Lecture
