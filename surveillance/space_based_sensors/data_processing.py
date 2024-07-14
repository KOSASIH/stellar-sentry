# surveillance/space_based_sensors/data_processing.py
import numpy as np
from astropy.io import fits

class SensorDataProcessor:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def process_data(self):
        # Process the sensor data using astropy
        hdul = fits.open(self.sensor_data)
        data = hdul[0].data
        return data

    def extract_features(self, data):
        # Extract features from the processed data
        features = []
        for i in range(data.shape[0]):
            features.append(np.mean(data[i]))
        return features
