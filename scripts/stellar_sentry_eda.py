import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(data):
    # Summary statistics
    print(data.describe())

    # Distribution plots
    sns.set()
    plt.figure(figsize=(12, 6))
    sns.distplot(data['semi_major_axis'])
    plt.title('Semi-Major Axis Distribution')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.distplot(data['eccentricity'])
    plt.title('Eccentricity Distribution')
    plt.show()

    # Correlation matrix
    corr_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.show()

def main():
    # Load data
    data = pd.read_csv('data/processed_data.csv')

    # Explore data
    explore_data(data)

if __name__ == '__main__':
    main()
