from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, precision_score, recall_score

# Initialize models
logistic_model = LogisticRegression(random_state=42)
random_forest_model = RandomForestClassifier(random_state=42)
gradient_boosting_model = GradientBoostingClassifier(random_state=42)

# List of models
models = [logistic_model, random_forest_model, gradient_boosting_model]
model_names = ['Logistic Regression', 'Random Forest', 'Gradient Boosting']

# Dictionary to store evaluation metrics
evaluation_metrics = {'Model': [], 'Accuracy': [], 'F1-Score': [], 'ROC AUC': [], 'Precision': [], 'Recall': []}

# Train and evaluate each model
for model, name in zip(models, model_names):
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on test set
    y_pred = model.predict(X_test)
    
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    
    # Store metrics
    evaluation_metrics['Model'].append(name)
    evaluation_metrics['Accuracy'].append(accuracy)
    evaluation_metrics['F1-Score'].append(f1)
    evaluation_metrics['ROC AUC'].append(roc_auc)
    evaluation_metrics['Precision'].append(precision)
    evaluation_metrics['Recall'].append(recall)

# Convert metrics to DataFrame for easy viewing
evaluation_df = pd.DataFrame(evaluation_metrics)

evaluation_df
