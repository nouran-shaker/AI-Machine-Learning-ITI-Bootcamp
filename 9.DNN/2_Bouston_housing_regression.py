import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import HeNormal

boston = fetch_openml(name='boston', version=1, as_frame=True, parser='auto')
X = boston.data
y = boston.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Input(shape=(X_train.shape[1],)))

for _ in range(7):
    model.add(Dense(64, activation='relu', kernel_initializer=HeNormal()))

model.add(Dense(1))

optimizer = Adam(learning_rate=0.001, clipnorm=1.0)
model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

loss, mae = model.evaluate(X_test, y_test)
print(f"Mean Absolute Error: ${mae * 1000:.2f}")