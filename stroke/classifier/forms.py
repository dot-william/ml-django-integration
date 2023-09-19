from classifier.models import IrisFeature
from django import forms

class IrisFeatureForm(forms.ModelForm):
    class Meta:
        model = IrisFeature
        fields = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        GENDER_CHOICES = (('Male','Male'), ('Female', 'Female'))

        HYPERTENSION_CHOICES = (('Yes', 1), ('No', 0)) 

        labels = {
            'age': '',
            'gender': '',
            'hypertension': '',
            'heart_disease': '',     
            'avg_glucose_level': '',
            'married': 'Married (Yes or No)',
            'bmi': ''
        }

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age'}),
            'gender': forms.Select(choices=GENDER_CHOICES),
            'hypertension': forms.Select(choices=HYPERTENSION_CHOICES),
            forms.NumberInput(attrs={'class': 'form-control', 'id': 'sepal_width'}),
            'petal_length': forms.NumberInput(attrs={'class': 'form-control', 'id': 'petal_length'}),
            'petal_width': forms.NumberInput(attrs={'class': 'form-control', 'id': 'petal_width'})
        }