# 🌟 Daily Hub

**Daily Hub** is a lightweight and modern dashboard that brings weather and news directly to your screen, making it perfect for in-home displays or as a daily companion on your computer.

## 🚀 Key Features

- **🌤️ Real-Time Weather**: Get the latest weather information for your city with data from OpenWeatherMap.
- **📰 Fresh News**: Stay updated with the latest news from your country, powered by NewsAPI.
- **⚡ Automatic Updates**: Data is fetched and displayed automatically, with no need for manual refreshes.
- **🔧 Easy to Set Up**: Just clone the repository, install dependencies, and you're ready to go!

## 📸 Preview

*(Add a screenshot of your dashboard here for a visual impact!)*

## 🛠️ Installation

Follow these simple steps to get **Daily Hub** running on your machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fazelucq1/daily-hub.git
   cd daily-hub
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   - Open the `.env` file.
   - Add your API keys for OpenWeatherMap and NewsAPI:
     ```env
     WEATHER_API_KEY=your_openweathermap_api_key
     NEWS_API_KEY=your_newsapi_api_key
     ```
   - Don't have the keys? Get them from [OpenWeatherMap](https://openweathermap.org/api) and [NewsAPI](https://newsapi.org).

4. **Run the Script**:
   ```bash
   python main.py
   ```

5. **View the Dashboard**:
   - The weather and news will be displayed in your terminal. Enjoy your new dashboard!
     `http://127.0.0.1:5000/`

## 🎛️ Customization

- **Change City**: Use the `--city` argument to get weather for a different city, e.g., `python main.py --city Milan`.
- **Change Country for News**: Use the `--country` argument to get news from a different country, e.g., `python main.py --country us`.


## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org) for weather data.
- [NewsAPI](https://newsapi.org) for real-time news.
- The open-source community for the amazing tools that make projects like this possible.

---

**Daily Hub** is your go-to daily dashboard for weather and news. Try it today and make your morning routine a little smarter! 🚀
