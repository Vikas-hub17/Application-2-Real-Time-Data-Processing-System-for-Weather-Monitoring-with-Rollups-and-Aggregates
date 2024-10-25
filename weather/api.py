import requests
from weather.db import store_weather_data

API_KEY = "2a461909a24e249f4bc91f0ff76cc00d"
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_and_store_weather(city):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        store_weather_data(city, data)
    else:
        raise Exception(f"Error fetching data for {city}: {data['message']}")
