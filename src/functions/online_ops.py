import requests
import pywhatkit as kit
import smtplib
from decouple import config

# NEWS_API_KEY = config("NEWS_API_KEY")
# OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
# TMDB_API_KEY = config("TMDB_API_KEY")
# EMAIL = config("EMAIL")
# PASSWORD = config("PASSWORD")


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)

# def get_latest_news():
#    news_headlines = []
#    res = requests.get(
#        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
#    articles = res["articles"]
#    for article in articles:
#        news_headlines.append(article["title"])
#    return news_headlines[:5]


# def get_weather_report(city):
#   res = requests.get(
#        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
#    weather = res["weather"][0]["main"]
#    temperature = res["main"]["temp"]
#    feels_like = res["main"]["feels_like"]
#    return weather, f"{temperature}℃", f"{feels_like}℃"

