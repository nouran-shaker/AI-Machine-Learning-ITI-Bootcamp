import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = pd.read_csv('data_banknote_authentication.txt')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(X.shape[1],))
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.005), 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

model.fit(X_train_scaled, y_train, epochs=100, validation_split=0.2, verbose=0)

y_pred_probs = model.predict(X_test_scaled)
y_pred = (y_pred_probs > 0.5).astype(int)

print(f"Banknote Authenticity Accuracy: {accuracy_score(y_test, y_pred):.4f}")