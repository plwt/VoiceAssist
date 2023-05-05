import subprocess
import pywhatkit
import webbrowser

import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup

# import smtplib
# from decouple import config
# import requests


def play_on_youtube(video):
    # Asks the user for a search term and presents results in YouTube
    pywhatkit.playonyt(video)

def search_on_google(query):
    # Asks the user for a search term and presents results in Google
    pywhatkit.search(query)

def open_news():
    # Opens the browser and displays news
    exit_code = subprocess.Popen(("xdg-open", "https://en.wikinews.org/wiki/Main_Page"))
    print(exit_code)

def open_weather():
    # Opens the browser and displays weather
    exit_code = subprocess.Popen(("xdg-open", "https://openweathermap.org/"))
    print(exit_code)
    
def open_maps():
    # Opens the browser and displays maps
    exit_code = subprocess.Popen(("xdg-open", "https://www.openstreetmap.org"))
    print(exit_code)
    
def easter_egg():
    # Too many secrets
    exit_code = subprocess.Popen(("xdg-open", "https://www.youtube.com/watch?v=uT7Q4exM0T0"))
    print(exit_code)

def easter_egg2():
    # Hack the planet
    exit_code = subprocess.Popen(("xdg-open", "https://threatbutt.com/map/"))
    print(exit_code)

def web_search(engine, query):
    search_terms = query.replace("computer", "").strip()
    url = f"https://www.perplexity.ai/search?q={query}"
    webbrowser.open(url)
