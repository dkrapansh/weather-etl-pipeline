import logging
from logger_config import *  # initializes logging
from extract import fetch_weather_data
from transform import transform_weather_data
from load import load_data_to_postgres

def main():
    logging.info("🔹 Starting ETL pipeline...")

    cities = ["London", "New York", "Tokyo", "Mumbai", "Paris"]

    logging.info("🔹 Extracting data...")
    raw_data = fetch_weather_data(cities)

    logging.info("🔹 Transforming data...")
    df = transform_weather_data(raw_data)
    logging.info(f"\n{df}")

    logging.info("🔹 Loading data to PostgreSQL...")
    load_data_to_postgres(df)

    logging.info("✅ ETL pipeline completed successfully!\n")

if __name__ == "__main__":
    main()
