import schedule
import time
from weather.api import get_weather_data
from weather.db import store_weather_data
from config import CITIES, FETCH_INTERVAL
from weather.processing import calculate_daily_summary

def fetch_and_store_weather():
    """
    Fetches weather data for all cities and stores it in the database.
    """
    for city in CITIES:
        weather_data = get_weather_data(city)
        if weather_data:
            store_weather_data(weather_data)

def start_schedule():
    """
    Schedules tasks to fetch weather data and calculate daily summaries.
    """
    schedule.every(FETCH_INTERVAL).minutes.do(fetch_and_store_weather)
    schedule.every().day.at("23:59").do(calculate_daily_summary)

    while True:
        schedule.run_pending()
        time.sleep(1)
