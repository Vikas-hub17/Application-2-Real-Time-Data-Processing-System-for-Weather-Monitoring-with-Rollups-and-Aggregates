from flask import Flask, render_template, request
from weather.api import fetch_and_store_weather
from weather.db import get_daily_summary, init_db
from visualizations.plot import plot_weather_trends

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch daily weather summary from the database
    summary = get_daily_summary()
    return render_template('index.html', summary=summary)

@app.route('/plot', methods=['POST'])
def plot():
    city = request.form['city']
    plot_weather_trends(city)
    return render_template('index.html', city=city, plot_generated=True)

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)
