# Generated by Django 4.2.5 on 2023-09-18 08:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IrisFeature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sepal_length",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.1)]
                    ),
                ),
                (
                    "sepal_width",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.1)]
                    ),
                ),
                (
                    "petal_length",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.1)]
                    ),
                ),
                (
                    "petal_width",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.1)]
                    ),
                ),
            ],
        ),
    ]
