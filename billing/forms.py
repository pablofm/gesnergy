from django import forms
from billing.models import Lecture, Pricing


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'
