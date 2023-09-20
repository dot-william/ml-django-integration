from django.template import loader
from django.http import HttpResponse
from classifier.forms import StrokeFeatureForm
from classifier.models import StrokeFeature
from classifier.apps import ClassifierConfig
import numpy as np
import pandas as pd


def home(request):
    template = loader.get_template("classifier/home.html")
    form = StrokeFeatureForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

def predict(request):
    """
        Retrieves the input from the form fields and
        passes the inputs to the model for prediction.
    """

    targets = ['No', 'Yes']

    if request.method == 'POST':
        form = StrokeFeatureForm(request.POST)

        if form.is_valid():
            
            # the features we want to get the prediction for
            age = int(form.cleaned_data.get('age'))
            gender = form.cleaned_data.get('gender')
            hypertension = int(form.cleaned_data.get('hypertension'))
            heart_disease = int(form.cleaned_data.get('heart_disease'))
            ever_married = form.cleaned_data.get('ever_married')
            work_type = form.cleaned_data.get('work_type')
            residence_type = form.cleaned_data.get('residence_type')
            avg_glucose_level = float(form.cleaned_data.get('avg_glucose_level'))
            bmi = float(form.cleaned_data.get('bmi'))
            smoking_status = form.cleaned_data.get('smoking_status')
            dict_features = {'gender':[gender], 'age': [age], 'hypertension': [hypertension],
                                    'heart_disease': [heart_disease], 'ever_married' : [ever_married],
                                    'work_type' : [work_type], 'Residence_type': [residence_type],
                                    'avg_glucose_level': [avg_glucose_level], 'bmi': [bmi], 'smoking_status': [smoking_status]}
            features = pd.DataFrame.from_dict(dict_features)
            print(features)
            # One hot encode
            categories = features.select_dtypes(include=['object']).columns
            ohe_df = ClassifierConfig.encoder.transform(features[categories])
            ohe_df = pd.DataFrame(ohe_df.toarray(), columns=ClassifierConfig.encoder.get_feature_names_out(categories))
            encoded_features_df = pd.concat([features, ohe_df], axis=1)
            encoded_features_df = encoded_features_df.drop(columns=categories)

            scaled_features= ClassifierConfig.scaler.transform(encoded_features_df)
            print(scaled_features)
            # pd.DataFrame(scaled_values, columns=stroke_df_copy.columns, index=stroke_df_copy.index)
            # # numerical_data = np.array(avg_glucose_level, bmi)
            # # categorical = np.array(gender, ever_married, work_type, residence_type, smoking_status)
            #  # encoded = ClassifierConfig.encoder.transform(categorical)
            # # scale_vals = ClassifierConfig.scaler.transform(numerical_data)
            # # encoded = ClassifierConfig.encoder.transform(categorical)

            
            # # [[1, 2, 3, 4]]
            # prediction = ClassifierConfig.model.predict(features.reshape(1, -1))[0]
            # prediction = targets[prediction]
            
            # prediction_probas = ClassifierConfig.calibrated_clf.predict_proba(features.reshape([1, -1]))[0]
            # prediction_probas = [f"{prob*100:.2f}%" for prob in prediction_probas]
            
          
            # prediction_proba_classes = zip(targets, prediction_probas)
            # prediction_proba_classes = sorted(prediction_proba_classes, key = lambda x: x[1], reverse=True)

    template = loader.get_template('classifier/home.html')
    context = {
        'form': form
    }
    # context = {
    #     'form': form,
    #     'predictions': prediction_proba_classes
    # }

    return HttpResponse(template.render(context, request))