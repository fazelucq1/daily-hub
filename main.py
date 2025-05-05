from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
CITIES = ["New York", "London", "Tokyo", "Paris", "Dubai", "Sydney", "Shanghai", "Sao Paulo", "Mumbai", "Moscow"]
COUNTRY = "it"
TIMEZONES = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Dubai": "Asia/Dubai",
    "Sydney": "Australia/Sydney",
    "Shanghai": "Asia/Shanghai",
    "Sao Paulo": "America/Sao_Paulo",
    "Mumbai": "Asia/Kolkata",
    "Moscow": "Europe/Moscow"
}
WEATHER_EMOJIS = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️"
}

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            weather_type = weather['main'].lower()
            emoji = WEATHER_EMOJIS.get(weather_type, "🌍")
            local_time = datetime.now(pytz.timezone(TIMEZONES[city])).strftime("%H:%M:%S")
            return {
                'city': city,
                'temperature': main['temp'],
                'feels_like': main['feels_like'],
                'humidity': main['humidity'],
                'pressure': main['pressure'],
                'description': weather['description'].capitalize(),
                'icon': weather['icon'],
                'wind_speed': wind['speed'],
                'emoji': emoji,
                'local_time': local_time
            }
        else:
            return {'city': city, 'error': f"Error: {response.status_code}"}
    except Exception as e:
        return {'city': city, 'error': str(e)}

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country={COUNTRY}&pageSize=5&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            if articles:
                return [{
                    'title': article['title'],
                    'description': article['description'] or "No description available.",
                    'url': article['url']
                } for article in articles]
            else:
                return [{'title': "No news available.", 'description': "", 'url': "#"}]
        else:
            return [{'title': f"Error: {response.status_code}", 'description': "", 'url': "#"}]
    except Exception as e:
        return [{'title': str(e), 'description': "", 'url': "#"}]

@app.route('/')
def dashboard():
    weather_data = [fetch_weather(city) for city in CITIES]
    news = fetch_news()
    return render_template('index.html', weather_data=weather_data, news=news)

if __name__ == '__main__':
    app.run(debug=True)
