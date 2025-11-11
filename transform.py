#rawAPI Json to clean Pandas df
import pandas as pd
import logging

def transform_weather_data(raw_data):
    if not raw_data:
        logging.warning("⚠️ No data received to transform.")
        return pd.DataFrame()

    transformed = []
    for item in raw_data:
        try:
            transformed.append({
                "city": item["name"],
                "temperature": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "pressure": item["main"]["pressure"],
                "weather": item["weather"][0]["description"],
                "wind_speed": item["wind"]["speed"]
            })
        except KeyError as e:
            logging.error(f"❌ Missing key during transformation: {e}")

    df = pd.DataFrame(transformed)
    logging.info(f"✅ Transformed data for {len(df)} cities.")
    return df
