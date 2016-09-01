from django import forms
from billing.models import Measure, Pricing


class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = '__all__'


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'
