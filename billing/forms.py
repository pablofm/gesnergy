from django import forms
from billing.models import Lecture, Pricing


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'

    def is_valid(self):
        valid = super(LectureForm, self).is_valid()
        # Los campos están vacíos
        if not valid:
            return False
        if Lecture.objects.count() > 0:
            if self.data["lecture"] < Lecture.objects.last().lecture:
                return False

        return True


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'
