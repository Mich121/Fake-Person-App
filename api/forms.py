from django import forms
from .models import Person

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'certificate': forms.TextInput(attrs={'class':'form-control'}),
            'university': forms.TextInput(attrs={'class':'form-control'}),
            'marriage': forms.CheckboxInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'religion': forms.TextInput(attrs={'class':'form-control'}),
        }

