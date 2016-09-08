from django import forms
from pricing.models import Pricing


class PricingForm(forms.ModelForm):
    def is_valid(self):
        valid = super(PricingForm, self).is_valid()
        if not valid:
            return False

        if self.data["price"] < 0:
            return False

        return True

    class Meta:
        model = Pricing
        fields = '__all__'
