from flask import Flask, render_template, request
import os, requests
from dotenv import load_dotenv
from .fetcher import WeatherDataFetcher

class WeatherDashboard:
    def __init__(self):
        self.app = Flask(__name__)
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.weather_fetcher = WeatherDataFetcher(self.api_key)
        self.add_routes()
        
    def add_routes(self):       
        @self.app.route('/', methods=["GET", "POST"])
        def index():
            city = request.form.get('city', 'Melbourne')
            weather_data = self.weather_fetcher.get_weather(city)
            return render_template('index.html', weather_data=weather_data)
    
    def run(self):
        self.app.run(debug=True,port=5001)
    
    