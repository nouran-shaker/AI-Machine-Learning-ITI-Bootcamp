import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = {
    'MSRP': [25000, 45000, 85000, 30000, 95000],
    'Highway_MPG': [35, 25, 18, 30, 20],
    'City_MPG': [28, 18, 12, 22, 14],
    'Vehicle_Style': ['Sedan', 'SUV', 'Sports Car', 'SUV', 'Sports Car']
}
cars = pd.DataFrame(data)

cars['Log_MSRP'] = np.log1p(cars['MSRP'])

cars_encoded = pd.get_dummies(cars, columns=['Vehicle_Style'], drop_first=True)

cars_encoded['Fuel_Efficiency'] = 0.5 * (cars_encoded['Highway_MPG'] + cars_encoded['City_MPG'])

X = cars_encoded.drop(['MSRP', 'Log_MSRP', 'Highway_MPG', 'City_MPG'], axis=1)
y = cars_encoded['Log_MSRP']

model = LinearRegression().fit(X, y)

coefficients = pd.Series(model.coef_, index=X.columns)
print("Model Coefficients:")
print(coefficients)

if 'Vehicle_Style_Sports Car' in coefficients and 'Vehicle_Style_SUV' in coefficients:
    sports_effect = coefficients['Vehicle_Style_Sports Car']
    suv_effect = coefficients['Vehicle_Style_SUV']
    
    log_diff = sports_effect - suv_effect
    premium_percentage = (np.exp(log_diff) - 1) * 100
    print(f"\nSports Cars are priced {premium_percentage:.2f}% higher than SUVs on average.")