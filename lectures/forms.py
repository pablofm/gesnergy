from django import forms
from lectures.models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'

    def is_valid(self):
        valid = super(LectureForm, self).is_valid()
        if not valid:
            return False
        if Lecture.objects.count() > 0:
            if self.data["lecture"] < Lecture.objects.last().lecture:
                return False

        return True
