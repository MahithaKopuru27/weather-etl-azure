# Weekly Weather ETL Pipeline (Azure + Tableau)

This project extracts, transforms, and visualizes weekly weather data using:

- **Python (ETL)** — Fetches weather data via Open-Meteo API.
- **Azure Blob Storage (planned)** — Stores transformed data.
- **Tableau** — Visualizes weekly temperature trends.

## Files
- `data_ingest.py` — Pulls raw data from API.
- `data_transform.py` — Aggregates and saves weekly data as CSV.
- `dashboard/Weekly_Weather_Trends.twb` — Tableau visualization dashboard.

## Dashboard KPIs
- Average Temperature (°C)
- Minimum Temperature (°C)
- Maximum Temperature (°C)

## Output
Displays a weekly temperature trend line and key weather statistics.

