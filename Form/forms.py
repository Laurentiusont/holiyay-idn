from django import forms
from .models import saran


class saranForm(forms.ModelForm):
    class Meta:
        model = saran
        fields = [
            'Nama',
            'isi',
        ]
