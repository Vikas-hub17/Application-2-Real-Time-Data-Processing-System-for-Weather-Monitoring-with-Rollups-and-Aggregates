from flask import Flask, render_template, request
from weather.api import fetch_and_store_weather
from weather.db import get_daily_summary, init_db
from weather.api import fetch_and_store_weather
from weather.db import init_db

# Initialize the database
init_db()

# Fetch weather data for 'Delhi'
fetch_and_store_weather('Delhi')

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Fetch daily weather summary from the database
        summary = get_daily_summary()
        if not summary:
            return "No data available yet. Try fetching weather data.", 500
        return render_template('index.html', summary=summary)
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/plot', methods=['POST'])
def plot():
    city = request.form['city']
    try:
        plot_weather_trends(city)
        return render_template('index.html', city=city, plot_generated=True)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)
