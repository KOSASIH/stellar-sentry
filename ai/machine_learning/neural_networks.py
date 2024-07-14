# ai/machine_learning/neural_networks.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class NeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.model = Sequential()
        self.model.add(Dense(hidden_dim, input_dim=input_dim, activation='relu'))
        self.model.add(Dense(output_dim, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train, epochs=10, batch_size=128)

    def predict(self, X_test):
        return self.model.predict(X_test)
