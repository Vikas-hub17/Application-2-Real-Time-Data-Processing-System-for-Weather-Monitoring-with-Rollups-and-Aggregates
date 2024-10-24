import sqlite3

def calculate_daily_summary():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT city, AVG(temp), MAX(temp), MIN(temp), COUNT(main), main
        FROM weather
        WHERE DATE(timestamp, 'unixepoch') = DATE('now')
        GROUP BY city, main
    ''')
    
    summary = cursor.fetchall()
    conn.close()
    return summary

def check_thresholds():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    threshold_temp = 35.0  # Example threshold: Alert if temp exceeds 35°C
    cursor.execute('''
        SELECT city, temp, main FROM weather WHERE temp > ? ORDER BY timestamp DESC
    ''', (threshold_temp,))
    
    alerts = cursor.fetchall()
    for alert in alerts:
        print(f"ALERT: {alert[0]} has a temperature of {alert[1]}°C with {alert[2]} condition.")
    
    conn.close()
