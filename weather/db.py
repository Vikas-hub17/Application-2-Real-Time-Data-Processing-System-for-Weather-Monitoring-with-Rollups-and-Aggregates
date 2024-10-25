import sqlite3

DATABASE = 'weather_data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                 id INTEGER PRIMARY KEY,
                 city TEXT,
                 temperature REAL,
                 condition TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def store_weather_data(city, data):
    temperature = data['main']['temp']
    condition = data['weather'][0]['description']
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO weather (city, temperature, condition) VALUES (?, ?, ?)',
              (city, temperature, condition))
    conn.commit()
    conn.close()

def get_daily_summary():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        SELECT city, AVG(temperature), MAX(temperature), MIN(temperature), 
        GROUP_CONCAT(DISTINCT condition)
        FROM weather
        WHERE timestamp >= date('now', 'start of day')
        GROUP BY city
    ''')
    summary = c.fetchall()
    conn.close()
    return summary

from weather.db import init_db
init_db()
