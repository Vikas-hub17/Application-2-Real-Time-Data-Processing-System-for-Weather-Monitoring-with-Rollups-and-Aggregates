import requests
import sqlite3
from config import API_KEY

def fetch_and_store_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        condition = data['weather'][0]['description']

        conn = sqlite3.connect('weather_data.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO weather (city, avg_temp, min_temp, max_temp, condition)
                          VALUES (?, ?, ?, ?, ?)''', (city, temp, temp_min, temp_max, condition))
        conn.commit()
        conn.close()
    else:
        print(f"Error fetching weather data for {city}: {response.status_code}")
