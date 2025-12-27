import requests
import pandas as pd
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 40.4093,
    "longitude": 49.8671,
    "daily": [
        "sunrise",
        "precipitation_sum",
        "temperature_2m_max",
        "weather_code",
        "temperature_2m_min"
    ],
    "timezone": "auto",
    "start_date": "2025-11-01",
    "end_date": "2025-12-25"
}


def extract_data():
    """
    Sends a GET request to Open-Meteo API with specified parameters.
    Returns:
        dict: JSON response from API containing daily weather data
    Raises:
        Exception: if the request fails
    """
    response = requests.get(url, params=params) 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


if __name__ == "__main__":
    data = extract_data()
    with open("data/raw/weather_data.json", "w") as f:
        json.dump(data, f)
        print("Data successfully extracted and saved to weather_data.json")
