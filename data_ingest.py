import requests
import json
from datetime import datetime, timedelta

# Dallas coordinates
latitude = 32.7767
longitude = -96.7970

# Calculate 7-day date range (from today)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=6)

# API endpoint (7-day forecast)
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&start_date={start_date}&end_date={end_date}&timezone=auto"

# Fetch data
response = requests.get(url)
data = response.json()

# Save to file
with open("raw_weather_week.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ 7-day weather data saved as raw_weather_week.json ({start_date} → {end_date})")
