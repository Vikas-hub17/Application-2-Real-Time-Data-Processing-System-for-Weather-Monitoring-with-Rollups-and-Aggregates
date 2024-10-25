import sqlite3
import matplotlib.pyplot as plt

def plot_weather_trends(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT avg_temp, min_temp, max_temp
        FROM weather
        WHERE city = ?
    ''', (city,))
    data = cursor.fetchall()
    conn.close()

    if data:
        avg_temps, min_temps, max_temps = zip(*data)
        plt.figure(figsize=(10, 5))
        plt.plot(avg_temps, label='Avg Temp (°C)', color='blue')
        plt.plot(min_temps, label='Min Temp (°C)', color='green')
        plt.plot(max_temps, label='Max Temp (°C)', color='red')
        plt.title(f'Temperature Trends for {city}')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.savefig(f'static/{city}_weather_trends.png')
    else:
        print(f"No data found for {city}")
