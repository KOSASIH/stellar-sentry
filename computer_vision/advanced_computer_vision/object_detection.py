# computer_vision/advanced_computer_vision/object_detection.py
import numpy as np
import cv2
from sklearn.cluster import DBSCAN

class ObjectDetection:
    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.edges = cv2.Canny(gray, 50, 150)

    def detect_edges(self):
        # Detect edges in the image using the Canny edge detector
        return self.edges

    def cluster_edges(self):
        # Cluster edges using DBSCAN
        edge_points = np.where(self.edges > 0)
        edge_points = np.array(edge_points).T
        dbscan = DBSCAN(eps=5, min_samples=10)
        labels = dbscan.fit_predict(edge_points)
        return labels

    def detect_objects(self, labels):
        # Detect objects in the image using the clustered edges
        objects = []
        for label in np.unique(labels):
            if label!= -1:
                object_points = edge_points[labels == label]
                x, y, w, h = cv2.boundingRect(object_points)
                objects.append((x,y, w, h))
        return objects
