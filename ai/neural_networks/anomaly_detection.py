# ai/neural_networks/anomaly_detection.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

class AnomalyDetector:
    def __init__(self, data):
        self.data = data
        self.model = self.create_model()

    def create_model(self):
        # Create a neural network model for anomaly detection
        model = Sequential()
        model.add(LSTM(50, input_shape=(self.data.shape[1], 1)))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train(self):
        # Train the neural network model
        self.model.fit(self.data, epochs=100, batch_size=32, validation_split=0.2)

    def detect_anomalies(self, input_data):
        # Detect anomalies using the trained model
        predictions = self.model.predict(input_data)
        anomalies = np.where(predictions > 0.5)[0]
        return anomalies
