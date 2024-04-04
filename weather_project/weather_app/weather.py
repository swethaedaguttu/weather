# weather_app/weather.py
import requests
from .config import API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'temperature': round(data['main']['temp'] - 273.15, 2),
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return {'error': 'Failed to fetch weather data'}
