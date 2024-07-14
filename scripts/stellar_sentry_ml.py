import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(data):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop("habitable", axis=1), data["habitable"], test_size=0.2, random_state=42)

    # Train random forest classifier
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    return rf

def predict_exoplanet(rf, exoplanet):
    # Use machine learning model to predict exoplanet properties
    prediction = rf.predict(exoplanet)
    return prediction

def main():
    # Load processed data
    data = pd.read_csv("data/processed_data.csv")

    # Train machine learning model
    rf = train_model(data)

    # Predict exoplanet properties
    exoplanet = pd.DataFrame([{
        "semi_major_axis": 0.42,
        "eccentricity": 0.01,
        "orbital_period": 267.3,
        # ...
    }])
    prediction = predict_exoplanet(rf, exoplanet)
    print(f"Exoplanet is likely to be {prediction}")

if __name__ == "__main__":
    main()
