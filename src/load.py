from transform import transform_data
import json
import pandas as pd



def load_data(df):
    """
    Loads the transformed DataFrame into a CSV file.

    Args:
        df (pandas.DataFrame): Transformed daily weather data
    """
    df.to_csv("data/processed/daily_weather_data.csv")
    print("Data successfully loaded to daily_weather_data.csv")



if __name__ == "__main__":
    with open("data/raw/weather_data.json", "r") as f:
        raw_data = json.load(f)
    
    df = transform_data(raw_data)
    load_data(df)