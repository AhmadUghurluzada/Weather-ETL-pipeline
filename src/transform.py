import json
import pandas as pd


def transform_data(raw_data):
    """
    Transforms raw weather JSON data into a clean daily DataFrame.

    Steps performed:
    - Normalizes daily weather data into tabular format
    - Converts time column to DatetimeIndex
    - Renames columns to consistent, readable names
    - Performs basic data quality checks and validations

    Args:
        raw_data (dict): Raw JSON response from Open-Meteo API

    Returns:
        pandas.DataFrame: Cleaned daily weather data indexed by date
    """
    df = pd.DataFrame(raw_data["daily"])
    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)
    
    df = df.rename(columns={
        "sunrise": "sunrise_time",
        "precipitation_sum": "precipitation_mm",
        "temperature_2m_max": "temp_max_c",
        "temperature_2m_min": "temp_min_c",
        "weather_code": "weather_code"
    })
    

    if df.isna().values.any():
        print("Warning: Missing values detected in the dataset.")
        print(df.isna().sum())

    
    if df.index.duplicated().any():
        print("Warning: Duplicate indices detected. Removing duplicates.")
        df = df[~df.index.duplicated(keep='first')]

    
    assert (df["temp_max_c"] >= df["temp_min_c"]).all(), "Invalid temperature range"
    assert (df["precipitation_mm"] >= 0).all(), "Negative precipitation detected"


    return df



if __name__ == "__main__":
    with open("data/raw/weather_data.json", "r") as f:
        raw_data = json.load(f)

    df = transform_data(raw_data)
    print(df.head())
    print(df.dtypes)