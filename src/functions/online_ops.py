# import requests
import pywhatkit

# import smtplib
# from decouple import config
import subprocess

#Asks the user for a search term and presents results in YouTube
def play_on_youtube(video):
    pywhatkit.playonyt(video)

#Asks the user for a search term and presents results in Google
def search_on_google(query):
    pywhatkit.search(query)

#Opens the browser and displays news
def open_news():
    exit_code = subprocess.Popen(("xdg-open", "https://en.wikinews.org/wiki/Main_Page"))
    print(exit_code)

#Opens the browser and displays weather
def open_weather():
    exit_code = subprocess.Popen(("xdg-open", "https://openweathermap.org/"))
    print(exit_code)
    
#Opens the browser and displays maps
def open_maps():
    exit_code = subprocess.Popen(("xdg-open", "https://www.openstreetmap.org"))
    print(exit_code)
