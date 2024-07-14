import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def process_data(data):
    """
    Processes and cleans the ingested data, including handling missing values and data normalization.

    Args:
        data (pandas.DataFrame): Ingested data

    Returns:
        pandas.DataFrame: Processed data
    """
    data.dropna(inplace=True)  # handle missing values
    scaler = StandardScaler()
    data[['feature1', 'feature2', 'feature3']] = scaler.fit_transform(data[['feature1', 'feature2', 'feature3']])

    return data

def main():
    data = pd.read_csv('data/processed_data.csv')
    processed_data = process_data(data)
    processed_data.to_csv('data/processed_data.csv', index=False)

if __name__ == '__main__':
    main()
