# ai/decision_support_system.py
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class DecisionSupportSystem:
    def __init__(self, data, features, target):
        self.data = data
        self.features = features
        self.target = target
        self.model = DecisionTreeClassifier()

    def train(self):
        # Train the decision tree model
        self.model.fit(self.data[self.features], self.data[self.target])

    def make_decision(self, input_data):
        # Make a decision using the trained model
        prediction = self.model.predict(input_data)
        return prediction
