from flask import Flask, render_template, request, jsonify
from weather.api import fetch_and_store_weather
from weather.db import get_daily_summary
from weather.schedule_tasks import start_schedule
from visualizations.plot import plot_weather_trends

app = Flask(__name__)

@app.route('/')
def index():
    # Get daily summary from the database
    summary = get_daily_summary()
    return render_template('index.html', summary=summary)

@app.route('/plot', methods=['POST'])
def plot():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    plot_weather_trends(city)
    return "Plot generated successfully!"

if __name__ == '__main__':
    # Start background scheduler to fetch data every 10 minutes
    start_schedule()
    app.run(debug=True)
