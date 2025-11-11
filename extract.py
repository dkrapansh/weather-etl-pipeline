import requests
import logging
from config import API_KEY

def fetch_weather_data(cities):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    all_data = []

    for city in cities:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            all_data.append(response.json())
            logging.info(f"✅ Successfully fetched data for {city}")
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Error fetching data for {city}: {e}")

    return all_data
