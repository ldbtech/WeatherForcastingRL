import pandas as pd
import numpy as np


def weather_flight_data():
    dataset = pd.read_csv("test_data.csv")
    weather_features = [
        "PRCP",
        "SNOW",
        "SNWD",
        "TMAX",
        "AWND",
        "LATITUDE",
        "LONGITUDE",
        "DEP_AIRPORT_HIST",
        "DAY_HISTORICAL",
        "DEP_DEL15",
    ]
    dataset = dataset[weather_features]
    dataset.dropna(inplace=True)

    return dataset


def get_weather_flight(flight_index, test_data):
    return test_data.iloc[flight_index][:-1].to_numpy()
