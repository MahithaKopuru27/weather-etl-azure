# transform.py
import json
import pandas as pd

def load_raw(filename="raw_weather.json"):
    """Read the raw JSON file"""
    with open(filename) as f:
        return json.load(f)

def to_dataframe(raw):
    """Convert JSON to a nice table (DataFrame)"""
    hourly = raw["hourly"]
    times = hourly["time"]
    temps = hourly["temperature_2m"]
    df = pd.DataFrame({"time": pd.to_datetime(times), "temp_c": temps})
    return df

def save_parquet(df, filename="weather_hourly.parquet"):
    """Save the cleaned data as Parquet file"""
    df.to_parquet(filename, index=False)

if __name__ == "__main__":
    raw = load_raw()
    df = to_dataframe(raw)
    save_parquet(df)
    print("✅ Saved clean data to weather_hourly.parquet")
