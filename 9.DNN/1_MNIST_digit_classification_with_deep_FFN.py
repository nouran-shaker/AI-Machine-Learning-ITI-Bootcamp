import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization
from tensorflow.keras.initializers import GlorotNormal
from tensorflow.keras.optimizers import Adam

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))

for _ in range(9):
    model.add(Dense(128, activation='sigmoid', kernel_initializer=GlorotNormal()))
    model.add(BatchNormalization())

model.add(Dense(10, activation='softmax'))

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=64, validation_split=0.2)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")