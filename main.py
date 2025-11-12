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
        # 🔹 Visualization step
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
        import psycopg2
        from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

        logging.info("📊 Generating visualization...")

        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=5432
        )

        query = "SELECT city, temperature, humidity, wind_speed FROM weather_data;"
        df = pd.read_sql(query, conn)
        conn.close()

        plt.figure(figsize=(7, 4))
        plt.bar(df["city"], df["temperature"], color='skyblue')
        plt.title("Temperature by City")
        plt.xlabel("City")
        plt.ylabel("Temperature (°C)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig("weather_plot.png")
        logging.info("📊 Visualization saved as weather_plot.png")

        logging.info("✅ Visualization displayed successfully!")

    except Exception as e:
        logging.error(f"❌ Visualization failed: {e}")

if __name__ == "__main__":
    main()
