import pandas as pd
import requests

def fetch_climate_disasters():
    # Placeholder simulated data — replace with real API fetch logic
    data = pd.DataFrame({
        "Region": ["California", "India", "Amazon", "Australia", "Japan"],
        "FireRisk": [0.9, 0.3, 0.95, 0.85, 0.2],
        "FloodRisk": [0.1, 0.7, 0.2, 0.1, 0.6],
        "DisplacementRisk": [0.05, 0.4, 0.3, 0.1, 0.2]
    })
    return data