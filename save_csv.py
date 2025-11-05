import pandas as pd

df = pd.read_parquet("weather_hourly.parquet")
df.to_csv("weather_hourly.csv", index=False)

print("✅ Saved weather_hourly.csv")
