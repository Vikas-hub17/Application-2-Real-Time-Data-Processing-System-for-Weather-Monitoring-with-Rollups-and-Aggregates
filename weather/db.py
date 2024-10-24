import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            timestamp INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(weather_data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, main, temp, feels_like, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (weather_data["city"], weather_data["main"], weather_data["temp"], weather_data["feels_like"], weather_data["dt"]))
    conn.commit()
    conn.close()
