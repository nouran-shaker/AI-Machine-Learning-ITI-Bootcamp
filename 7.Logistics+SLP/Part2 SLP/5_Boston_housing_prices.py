import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

california = fetch_california_housing(as_frame=True)
data = california.frame

X = data.drop('MedHouseVal', axis=1)
y = data['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(1, activation='linear', input_shape=(X.shape[1],))
])

model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.01), loss='mean_squared_error')
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, verbose=0)

y_pred = model.predict(X_test_scaled)
print(f"Boston Housing MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"Boston Housing R2 Score: {r2_score(y_test, y_pred):.4f}")