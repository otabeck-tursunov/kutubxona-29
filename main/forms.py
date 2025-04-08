from django import forms
from .models import *


# class TalabaForm(forms.Form):
#     ism = forms.CharField(required=True)
#     guruh = forms.CharField(required=True)
#     kurs = forms.IntegerField()
#     kitob_soni = forms.IntegerField()
#
#     def clean_kitob_soni(self):
#         kitob_soni = self.cleaned_data['kitob_soni']
#         if kitob_soni < 0:
#             raise forms.ValidationError("Kitob soni kamida 0 bo'lishi kerak")
#         return kitob_soni
#
#     def clean_kurs(self):
#         kurs = self.cleaned_data['kurs']
#         if kurs < 1 or kurs > 4:
#             raise forms.ValidationError("Kurs kamida 1-4 oralig'ida bo'lishi kerak!")
#         return kurs

class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = "__all__"


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

    def clean_t_sana(self):
        t_sana = self.cleaned_data['t_sana']
        if str(t_sana) < '1900-01-01':
            raise forms.ValidationError("Bu davrdagi mualliflar kiritilmaydi!")
        return t_sana


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"
