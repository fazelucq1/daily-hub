# 🌟 Daily Hub

**Daily Hub** is a lightweight and modern dashboard that brings weather and news directly to your screen, making it perfect for in-home displays or as a daily companion on your computer. Built with Python, it offers a smooth and visually appealing experience, with real-time updates and elegant formatting using the `rich` library.

## 🚀 Key Features

- **🌤️ Real-Time Weather**: Get the latest weather information for your city with data from OpenWeatherMap.
- **📰 Fresh News**: Stay updated with the latest news from your country, powered by NewsAPI.
- **🎨 Modern Design**: A clean and responsive interface, formatted beautifully in the terminal using `rich`.
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
   - Rename `.env.example` to `.env`.
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

## 🎛️ Customization

- **Change City**: Use the `--city` argument to get weather for a different city, e.g., `python main.py --city Milan`.
- **Change Country for News**: Use the `--country` argument to get news from a different country, e.g., `python main.py --country us`.
- **Style and Layout**: Modify the `rich` panels and formatting in `main.py` to customize the appearance.

## 🧑‍💻 Technologies Used

- **Python**: The core language for the script.
- **requests**: For making API calls to fetch weather and news data.
- **python-dotenv**: For managing environment variables.
- **rich**: For beautiful formatting in the terminal.

## 🤝 Contribute

Want to make **Daily Hub** even better? Great! Here's how you can contribute:

1. **Fork the Repository**.
2. **Create a Branch** for your feature (`git checkout -b feature/new-feature`).
3. **Commit Your Changes** (`git commit -m 'Added new feature'`).
4. **Push the Branch** (`git push origin feature/new-feature`).
5. **Open a Pull Request**.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org) for weather data.
- [NewsAPI](https://newsapi.org) for real-time news.
- The open-source community for the amazing tools that make projects like this possible.

---

**Daily Hub** is your go-to daily dashboard for weather and news. Try it today and make your morning routine a little smarter! 🚀
