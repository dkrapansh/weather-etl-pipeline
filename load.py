import psycopg2
import logging
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

def load_data_to_postgres(df):
    if df.empty:
        logging.warning("⚠️ No data to load into PostgreSQL.")
        return

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT,
                temperature FLOAT,
                humidity INT,
                pressure INT,
                weather TEXT,
                wind_speed FLOAT
            )
        """)

        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO weather_data (city, temperature, humidity, pressure, weather, wind_speed)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row.city, row.temperature, row.humidity, row.pressure, row.weather, row.wind_speed))

        conn.commit()
        cur.close()
        conn.close()

        logging.info(f"✅ Successfully loaded {len(df)} records into PostgreSQL.")
    except Exception as e:
        logging.error(f"❌ Error loading data into PostgreSQL: {e}")
