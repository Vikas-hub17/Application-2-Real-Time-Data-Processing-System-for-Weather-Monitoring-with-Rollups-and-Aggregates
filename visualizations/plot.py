import sqlite3
import matplotlib.pyplot as plt

def plot_weather_trends(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT DATE(timestamp, 'unixepoch'), AVG(temp), MAX(temp), MIN(temp)
        FROM weather
        WHERE city = ?
        GROUP BY DATE(timestamp, 'unixepoch')
    ''', (city,))
    
    data = cursor.fetchall()
    conn.close()
    
    dates = [row[0] for row in data]
    avg_temps = [row[1] for row in data]
    max_temps = [row[2] for row in data]
    min_temps = [row[3] for row in data]
    
    plt.plot(dates, avg_temps, label="Average Temp")
    plt.plot(dates, max_temps, label="Max Temp")
    plt.plot(dates, min_temps, label="Min Temp")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Daily Temperature Trends in {city}")
    plt.legend()
    plt.show()
