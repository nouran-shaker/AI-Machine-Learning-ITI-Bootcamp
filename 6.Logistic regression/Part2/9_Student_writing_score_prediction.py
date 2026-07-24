import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'MathScore': [70, 85, 90, 60, 88],
    'ReadingScore': [80, 90, 85, 65, 92],
    'Gender': ['female', 'male', 'female', 'male', 'female'],
    'TestPrep': ['none', 'completed', 'none', 'none', 'completed'],
    'WritingScore': [75, 88, 89, 60, 95]
})

data['TotalScore'] = data['MathScore'] + data['ReadingScore']

data_encoded = pd.get_dummies(data, columns=['Gender', 'TestPrep'])

X = data_encoded.drop(['WritingScore'], axis=1)
y = data['WritingScore']

model = LinearRegression().fit(X, y)

coef_dict = dict(zip(X.columns, model.coef_))
print(f"Gender_male Coefficient: {coef_dict.get('Gender_male', 0):.2f}")

new_student = pd.DataFrame({
    'MathScore': [85],
    'ReadingScore': [90],
    'TotalScore': [175],
    'Gender_female': [1],
    'Gender_male': [0],
    'TestPrep_completed': [1],
    'TestPrep_none': [0]
})

new_student = new_student[X.columns]
prediction = model.predict(new_student)

print(f"Expected Writing Score: {prediction[0]:.2f}")