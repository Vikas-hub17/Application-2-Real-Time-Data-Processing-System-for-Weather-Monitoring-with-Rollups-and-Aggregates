import requests
from config import API_KEY

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "main": data["weather"][0]["main"],
            "temp": kelvin_to_celsius(data["main"]["temp"]),
            "feels_like": kelvin_to_celsius(data["main"]["feels_like"]),
            "dt": data["dt"]
        }
    else:
        print(f"Failed to fetch data for {city}")
        return None
