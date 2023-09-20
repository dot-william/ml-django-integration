from classifier.models import StrokeFeature
from django import forms

class StrokeFeatureForm(forms.ModelForm):
    class Meta:
        fields = ('gender', 'age', 'hypertension', 'heart_disease','ever_married', 'work_type', 'residence_type','avg_glucose_level','bmi', 'smoking_status')

        model = StrokeFeature
        labels = {
            'age': 'Age', 
            'gender': 'Gender (Male of Female)', 
            'hypertension': 'Hypertension' , 
            'heart_disease': 'Heart Disease',
            'ever_married':  'Married',
            'work_type':  'Work Type',
            'residence_type':  'Residence Type',
            'avg_glucose_level': 'Glucose Level (mmol/L)',
            'bmi': 'BMI',
            'smoking_status': 'Smoking Status' 
        }

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'hypertension': forms.Select(attrs={'class': 'form-control', 'id': 'age'}),
            'heart_disease': forms.Select(attrs={'class': 'form-control', 'id': 'heart_disease'}),
            'ever_married': forms.Select(attrs={'class': 'form-control', 'id': 'ever_married'}),
            'work_type':  forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'residence_type': forms.Select(attrs={'class': 'form-control', 'id':'residence_type'}) ,
            'avg_glucose_level':  forms.NumberInput(attrs={'class': 'form-control', 'id': 'avg_glucose_level'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'id': 'bmi'}),
            'smoking_status': forms.Select(attrs={'class':'form-control', 'id':'smoking_status'})
        }