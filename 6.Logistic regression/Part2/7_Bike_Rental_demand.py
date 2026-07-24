import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'hour': [8, 12, 18, 2, 17],
    'weather': ['Clear', 'Rain', 'HeavyRain', 'Clear', 'Cloudy'],
    'season': ['Spring', 'Summer', 'Fall', 'Winter', 'Summer'],
    'demand': [400, 250, 20, 10, 500]
})

data['hour_sin'] = np.sin(2 * np.pi * data['hour'] / 24)
data['hour_cos'] = np.cos(2 * np.pi * data['hour'] / 24)

data_encoded = pd.get_dummies(data, columns=['weather', 'season'])

X = data_encoded.drop(['hour', 'demand'], axis=1)
y = data['demand']

model = LinearRegression().fit(X, y)

if 'weather_HeavyRain' in X.columns:
    idx = list(X.columns).index('weather_HeavyRain')
    demand_drop = model.coef_[idx]
    print(f"Demand change during heavy rain: {demand_drop:.2f} units")