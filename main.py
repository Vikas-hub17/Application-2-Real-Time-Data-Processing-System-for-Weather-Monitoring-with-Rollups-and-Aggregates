from weather.api import fetch_and_store_weather
from weather.schedule_tasks import start_schedule

if __name__ == "__main__":
    start_schedule()  # Start the scheduled tasks for fetching weather data
