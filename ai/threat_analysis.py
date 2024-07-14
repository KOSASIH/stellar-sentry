# ai/threat_analysis.py
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class ThreatAnalysis:
    def __init__(self, data):
        self.data = data
        self.model = self._create_model()

    def _create_model(self):
        model = Sequential()
        model.add(Dense(64, activation='relu', input_shape=(10,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def analyze(self):
        X = self.data.drop(['threat_level'], axis=1)
        y = self.data['threat_level']
        self.model.fit(X, y, epochs=10, batch_size=32)
        predictions = self.model.predict(X)
        return predictions
