from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
CITY = "Milan"
COUNTRY = "it"

def fetch_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            return {
                'city': CITY,
                'temperature': main['temp'],
                'description': weather['description'].capitalize(),
                'icon': weather['icon']
            }
        else:
            return {'error': f"Error: {response.status_code}"}
    except Exception as e:
        return {'error': str(e)}

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
    weather = fetch_weather()
    news = fetch_news()
    return render_template('index.html', weather=weather, news=news)

if __name__ == '__main__':
    app.run(debug=True)
