# ai/anomaly_detection.py
import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, data):
        self.data = data
        self.model = self._create_model()

    def _create_model(self):
        model = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.1)
        # model = IsolationForest(contamination=0.1)
        return model

    def detect_anomalies(self):
        X = self.data.drop(['timestamp'], axis=1)
        self.model.fit(X)
        anomalies = self.model.predict(X)
        return anomalies
