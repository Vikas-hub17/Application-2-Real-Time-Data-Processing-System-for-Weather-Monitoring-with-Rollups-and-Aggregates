import sqlite3

DATABASE = 'weather_data.db'

def calculate_daily_summary():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        SELECT city, AVG(temperature), MAX(temperature), MIN(temperature)
        FROM weather
        WHERE timestamp >= date('now', 'start of day')
        GROUP BY city
    ''')
    daily_summary = c.fetchall()
    conn.close()
    return daily_summary
