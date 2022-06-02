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