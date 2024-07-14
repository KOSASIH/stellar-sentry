import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

class ThreatAnalysis:
    def __init__(self, data):
        self.data = data
        self.model = self._create_model()

    def _create_model(self):
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(10, 1)))
        model.add(LSTM(units=50))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def analyze(self):
        X = self.data.drop(['threat_level'], axis=1)
        y = self.data['threat_level']
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        self.model.fit(X_scaled, y, epochs=10, batch_size=32)
        predictions = self.model.predict(X_scaled)
        return predictions

    def evaluate(self):
        y_pred = self.model.predict(self.data.drop(['threat_level'], axis=1))
        y_true = self.data['threat_level']
        accuracy = np.mean(y_pred == y_true)
        return accuracy
