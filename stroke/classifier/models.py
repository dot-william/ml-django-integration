from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class IrisFeature(models.Model):
    sepal_length = models.FloatField(validators=[MinValueValidator(0.1)])
    sepal_width = models.FloatField(validators=[MinValueValidator(0.1)])
    petal_length = models.FloatField(validators=[MinValueValidator(0.1)])
    petal_width = models.FloatField(validators=[MinValueValidator(0.1)])