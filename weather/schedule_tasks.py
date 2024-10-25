import schedule
import time
from weather.api import fetch_and_store_weather

CITIES = ['Delhi', 'New York', 'London', 'Tokyo']

def fetch_weather_for_all_cities():
    for city in CITIES:
        try:
            fetch_and_store_weather(city)
        except Exception as e:
            print(f"Error fetching weather for {city}: {e}")

def start_schedule():
    schedule.every(10).minutes.do(fetch_weather_for_all_cities)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
