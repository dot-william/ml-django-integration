from classifier.models import IrisFeature
from django import forms

class IrisFeatureForm(forms.ModelForm):
    class Meta:
        model = IrisFeature
        fields = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')

        labels = {
            'sepal_length': 'Sepal Length (cm)',
            'sepal_width': 'Sepal Width (cm)',
            'petal_length': 'Petal Length (cm)',
            'petal_width': 'Petal Width (cm)'
        }

        widgets = {
            'sepal_length': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sepal_length'}),
            'sepal_width': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sepal_width'}),
            'petal_length': forms.NumberInput(attrs={'class': 'form-control', 'id': 'petal_length'}),
            'petal_width': forms.NumberInput(attrs={'class': 'form-control', 'id': 'petal_width'})
        }