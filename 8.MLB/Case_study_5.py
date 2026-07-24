import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score

data = pd.read_csv('Telco-Customer-Churn.csv')

np.random.seed(42)
data = pd.DataFrame({
    'tenure': np.random.randint(1, 72, 500),
    'MonthlyCharges': np.random.uniform(20, 120, 500),
    'TotalCharges': np.random.uniform(20, 8000, 500),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], 500),
    'Churn': np.random.choice(['Yes', 'No'], 500)
})

data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce').fillna(0)
data['Churn'] = LabelEncoder().fit_transform(data['Churn'])
data = pd.get_dummies(data, drop_first=True)

X = data.drop('Churn', axis=1)
y = data['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp_churn = MLPClassifier(hidden_layer_sizes=(32,), solver='adam', max_iter=1000, random_state=42)
param_grid = {
    'alpha': [0.0001, 0.001, 0.01],
    'learning_rate_init': [0.001, 0.01]
}

grid = GridSearchCV(mlp_churn, param_grid, cv=3, scoring='roc_auc')
grid.fit(X_train_scaled, y_train)

best_model = grid.best_estimator_
y_pred_probs = best_model.predict_proba(X_test_scaled)[:, 1]

print("Best Hyperparameters:", grid.best_params_)
print("ROC-AUC Score:", roc_auc_score(y_test, y_pred_probs))