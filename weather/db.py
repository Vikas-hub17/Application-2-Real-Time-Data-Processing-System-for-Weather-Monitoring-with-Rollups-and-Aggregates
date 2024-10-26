import sqlite3

def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Create the weather table with the correct schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            avg_temp REAL NOT NULL,  -- Average temperature
            min_temp REAL NOT NULL,  -- Minimum temperature
            max_temp REAL NOT NULL,  -- Maximum temperature
            condition TEXT NOT NULL  -- Weather condition
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
