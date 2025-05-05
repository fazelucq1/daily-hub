import os
import requests
import argparse
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

load_dotenv()

console = Console()

def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            return f"Temperature: {main['temp']}°C\nDescription: {weather['description']}"
        elif response.status_code == 404:
            return "City not found."
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"

def fetch_news(api_key, country):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&pageSize=5&apiKey={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            if articles:
                return [f"{article['title']}\n{article['description']}" for article in articles]
            else:
                return ["No news available."]
        else:
            return [f"Error: {response.status_code}"]
    except Exception as e:
        return [f"Exception: {str(e)}"]

def main():
    parser = argparse.ArgumentParser(description="Smart Home Dashboard")
    parser.add_argument("--city", default="Rome", help="City for weather")
    parser.add_argument("--country", default="it", help="Country code for news")
    args = parser.parse_args()

    weather_api_key = os.getenv("WEATHER_API_KEY")
    news_api_key = os.getenv("NEWS_API_KEY")
    if not weather_api_key or not news_api_key:
        console.print("[red]Please set WEATHER_API_KEY and NEWS_API_KEY in .env file.[/red]")
        return

    weather = fetch_weather(weather_api_key, args.city)
    news = fetch_news(news_api_key, args.country)

    console.print(Panel(weather, title=f"Weather in {args.city}", expand=False))
    for i, item in enumerate(news, 1):
        console.print(Panel(item, title=f"News {i}", expand=False))

if __name__ == "__main__":
    main()
