import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            avg_temp REAL,
            min_temp REAL,
            max_temp REAL,
            condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_daily_summary():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT city, AVG(avg_temp), MAX(max_temp), MIN(min_temp), condition
        FROM weather
        GROUP BY city
    ''')
    summary = cursor.fetchall()
    conn.close()
    return summary
