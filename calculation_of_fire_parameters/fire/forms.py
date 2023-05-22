from django import forms

from .models import Fire


class FireForm(forms.ModelForm):
    class Meta:
        model = Fire
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
