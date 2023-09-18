from django.apps import AppConfig
from django.conf import settings
import joblib
import os


class ClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classifier'

    model = joblib.load(os.path.join(settings.BASE_DIR, 
                                     "models/iris_clf.joblib"))
    
    calibrated_clf = joblib.load(os.path.join(settings.BASE_DIR,
                                              "models/iris_calibrated_clf.joblib"))
