from django.template import loader
from django.http import HttpResponse
from classifier.forms import IrisFeatureForm
from classifier.models import IrisFeature
from classifier.apps import ClassifierConfig
import numpy as np



def home(request):
    template = loader.get_template("classifier/home.html")
    form = IrisFeatureForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

def predict(request):
    """
        Retrieves the input from the form fields and
        passes the inputs to the model for prediction.
    """

    targets = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

    if request.method == 'POST':
        form = IrisFeatureForm(request.POST)

        if form.is_valid():
            
            # the features we want to get the prediction for
            sepal_length = float(form.cleaned_data.get('sepal_length'))
            sepal_width = float(form.cleaned_data.get('sepal_width'))
            petal_length = float(form.cleaned_data.get('petal_length'))
            petal_width = float(form.cleaned_data.get('petal_width'))

            print(type(sepal_length))
            print(sepal_length, sepal_width, petal_length, petal_width)

            features = np.array([sepal_length, sepal_width, 
                                 petal_length, petal_width])
            # [[1, 2, 3, 4]]
            prediction = ClassifierConfig.model.predict(features.reshape(1, -1))[0]
            prediction = targets[prediction]

            prediction_probas = ClassifierConfig.calibrated_clf.predict_proba(features.reshape([1, -1]))[0]
            prediction_probas = [f"{prob*100:.2f}%" for prob in prediction_probas]
            
            # [('Iris Setosa', 30%), ('Iris Versicolor', 50%), ('Iris Virgnica', 20%)]
            prediction_proba_classes = zip(targets, prediction_probas)
            prediction_proba_classes = sorted(prediction_proba_classes, key = lambda x: x[1], reverse=True)

    template = loader.get_template('classifier/home.html')
    context = {
        'form': form,
        'predictions': prediction_proba_classes
    }

    return HttpResponse(template.render(context, request))