import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data(data):
    """
    Visualizes the processed data, including plots of exoplanet orbits and stellar properties.

    Args:
        data (pandas.DataFrame): Processed data
    """
    sns.set_style('whitegrid')

    # Plot exoplanet orbits
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='semi_major_axis', y='eccentricity', data=data)
    plt.title('Exoplanet Orbits')
    plt.xlabel('Semi-Major Axis (AU)')
    plt.ylabel('Eccentricity')
    plt.show()

    # Plot stellar properties
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='effective_temperature', y='surface_gravity', data=data)
    plt.title('Stellar Properties')
    plt.xlabel('Effective Temperature (K)')
    plt.ylabel('Surface Gravity (log(g))')
    plt.show()

def main():
    data = pd.read_csv('data/processed_data.csv')
    visualize_data(data)

if __name__ == '__main__':
    main()
