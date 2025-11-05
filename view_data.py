import pandas as pd

# Read the parquet file
df = pd.read_parquet("weather_hourly.parquet")

# Display first few rows
print(df.head())
