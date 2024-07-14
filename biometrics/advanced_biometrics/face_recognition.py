# biometrics/advanced_biometrics/face_recognition.py
import numpy as np
import cv2
from sklearn.svm import SVC

class FaceRecognition:
    def __init__(self, dataset):
        self.dataset = dataset
        self.X = dataset.drop('label', axis=1)
        self.y = dataset['label']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = SVC(kernel='linear', probability=True)

    def train(self):
        # Train the face recognition model
        self.model.fit(self.X_train, self.y_train)

    def predict(self, input_image):
        # Predict the identity of the person in the input image
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (224, 224))
            face = face.reshape((1, 224, 224))
            output = self.model.predict_proba(face)
            return output

    def evaluate(self):
        # Evaluate the performance of the face recognition model
        accuracy = self.model.score(self.X_test, self.y_test)
        return accuracy
