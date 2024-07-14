import pandas as pd
import numpy as np
from astropy.io import fits

def ingest_data(file_path):
    """
    Ingests data from various astronomical sources, including NASA's Exoplanet Archive and the Sloan Digital Sky Survey.

    Args:
        file_path (str): Path to the data file

    Returns:
        pandas.DataFrame: Ingested data
    """
    if file_path.endswith('.fits'):
        data = fits.open(file_path)[1].data
    elif file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format")

    return data

def main():
    file_path = 'data/exoplanet_archive.fits'
    data = ingest_data(file_path)
    print(data.head())

if __name__ == '__main__':
    main()
