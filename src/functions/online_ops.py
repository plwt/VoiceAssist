import subprocess
import pywhatkit

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
