import json
import pandas as pd

# Step 1: Read the raw 7-day data
with open("raw_weather_week.json", "r") as f:
    data = json.load(f)

# Step 2: Extract time and temperature into a DataFrame
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"]
})

# Step 3: Convert 'time' to datetime
df["time"] = pd.to_datetime(df["time"])

# Step 4: Extract date only (ignore hour)
df["date"] = df["time"].dt.date

# Step 5: Group by date to get daily average temperature
daily_avg = df.groupby("date", as_index=False)["temperature_2m"].mean()

# Step 6: Save the cleaned data as parquet
daily_avg.to_parquet("daily_weather.parquet", index=False)

print("✅ Weekly daily averages saved as daily_weather.parquet")
print(daily_avg)

# Convert Parquet to CSV for Tableau Public
daily_avg.to_csv("daily_weather.csv", index=False)
print("✅ Converted to CSV for Tableau Public")

