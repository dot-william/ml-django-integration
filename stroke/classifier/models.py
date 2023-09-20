from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, DecimalValidator

# Create your models here.
class StrokeFeature(models.Model):
    GENDER_CHOICES = (('Male','Male'), ('Female', 'Female'))

    YES_NO_CHOICES = ((1, 'Yes'), (0, 'No')) 
    MARRIED_CHOICES = (('Yes', 'Yes'), ('No', 'No')) 
    SMOKED_CHOICES = (('formerly smoked','formerly smoked'), ('never smoked','never smoked'), ('smokes','smokes'))
    RESIDENCE_TYPE = (('Urban', 'Urban'), ('Rural', 'Rural'))
    WORK_TYPE = (('Private','Private'), ('Self-employed','Self-employed'), ('Govt_job', 'Govt_job'), ('children','children'), ('Never_worked', 'Never_worked'))

    gender = models.CharField(choices=GENDER_CHOICES, max_length=50) 
    age = models.IntegerField(validators=[MinValueValidator(0.1)])
    hypertension = models.IntegerField(choices=YES_NO_CHOICES)
    heart_disease = models.IntegerField(choices=YES_NO_CHOICES)
    ever_married = models.CharField(choices=MARRIED_CHOICES, max_length=50) 
    work_type = models.CharField(choices=WORK_TYPE,  max_length=50) 
    residence_type = models.CharField(choices=RESIDENCE_TYPE,  max_length=50) 
    avg_glucose_level = models.FloatField(validators=[MinValueValidator(0.1)])
    bmi = models.FloatField(validators=[MinValueValidator(0.1)])
    smoking_status = models.CharField(choices=SMOKED_CHOICES,  max_length=50)