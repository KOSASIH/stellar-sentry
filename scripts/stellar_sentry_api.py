from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Exoplanet(BaseModel):
    name: str
    semi_major_axis: float
    eccentricity: float
    orbital_period: float

class StellarSystem(BaseModel):
    name: str
    exoplanets: List[Exoplanet]

@app.get("/exoplanets/")
async def read_exoplanets():
    # Retrieve exoplanet data from database or API
    exoplanets = [
        Exoplanet(name="Kepler-62f", semi_major_axis=0.42, eccentricity=0.01, orbital_period=267.3),
        Exoplanet(name="TRAPPIST-1e", semi_major_axis=0.03, eccentricity=0.005, orbital_period=6.1),
    ]
    return {"exoplanets": exoplanets}

@app.get("/stellar_systems/")
async def read_stellar_systems():
    # Retrieve stellar system data from database or API
    stellar_systems = [
        StellarSystem(name="Kepler-62", exoplanets=[
            Exoplanet(name="Kepler-62f", semi_major_axis=0.42, eccentricity=0.01, orbital_period=267.3),
            Exoplanet(name="Kepler-62g", semi_major_axis=0.51, eccentricity=0.02, orbital_period=356.2),
        ]),
        StellarSystem(name="TRAPPIST-1", exoplanets=[
            Exoplanet(name="TRAPPIST-1e", semi_major_axis=0.03, eccentricity=0.005, orbital_period=6.1),
            Exoplanet(name="TRAPPIST-1f", semi_major_axis=0.04, eccentricity=0.01, orbital_period=9.2),
        ]),
    ]
    return {"stellar_systems": stellar_systems}

@app.post("/predict/")
async def predict_exoplanet(exoplanet: Exoplanet):
    # Use machine learning model to predict exoplanet properties
    # ...
    return {"prediction": "Exoplanet is likely to be habitable"}
