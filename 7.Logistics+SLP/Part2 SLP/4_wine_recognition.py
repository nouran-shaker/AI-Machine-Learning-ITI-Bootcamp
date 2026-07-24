import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

wine = load_wine()
data = pd.DataFrame(wine.data, columns=wine.feature_names)
data['quality_label'] = wine.target

X = data.drop('quality_label', axis=1)
y = data['quality_label'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(3, activation='softmax', input_shape=(X.shape[1],))
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train, epochs=150, batch_size=16, verbose=0)

loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Wine Recognition Multi-class Accuracy: {accuracy:.4f}")