import matplotlib.pyplot as plt
import sqlite3

DATABASE = 'weather_data.db'

def plot_weather_trends(city):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        SELECT timestamp, temperature
        FROM weather
        WHERE city = ?
        ORDER BY timestamp
    ''', (city,))
    data = c.fetchall()
    conn.close()

    if not data:
        raise ValueError(f"No data available for {city}")

    timestamps, temperatures = zip(*data)
    plt.plot(timestamps, temperatures, label=city)
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Trend for {city}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{city}_trend.png')
