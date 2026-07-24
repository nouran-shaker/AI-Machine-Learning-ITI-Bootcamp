import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Age': [19, 18, 28, 33, 60, 30],
    'BMI': [27.9, 33.7, 33.0, 22.7, 30.0, 30.0],
    'Smoker': ['yes', 'no', 'no', 'no', 'no', 'no'],
    'Region': ['southwest', 'southeast', 'southeast', 'northwest', 'northeast', 'northeast'],
    'Cost': [16884, 1725, 4449, 21984, 12000, 5000]
})

data['Smoker_Binary'] = data['Smoker'].map({'yes': 1, 'no': 0})
data['Smoker_BMI_Int'] = data['Smoker_Binary'] * data['BMI']

data_encoded = pd.get_dummies(data, columns=['Region'], drop_first=True)

X_base = data_encoded.drop(['Smoker', 'Cost', 'Smoker_BMI_Int'], axis=1)
X_int = data_encoded.drop(['Smoker', 'Cost'], axis=1)
y = data['Cost']

model_base = LinearRegression().fit(X_base, y)
model_int = LinearRegression().fit(X_int, y)

coef_int = dict(zip(X_int.columns, model_int.coef_))

smoker_effect = coef_int.get('Smoker_Binary', 0) + (coef_int.get('Smoker_BMI_Int', 0) * 30)
print(f"Cost difference (Smoker vs Non-Smoker at BMI 30): ${smoker_effect:,.2f}")

age_effect = coef_int.get('Age', 0) * (60 - 30)
print(f"Cost difference (60-year-old vs 30-year-old): ${age_effect:,.2f}")