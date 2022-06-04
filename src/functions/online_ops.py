#import requests
import pywhatkit
#import smtplib
#from decouple import config
import subprocess


def play_on_youtube(video):
    pywhatkit.playonyt(video)

def search_on_google(query):
    pywhatkit.search(query)

def open_news():
    exit_code=subprocess.Popen(("xdg-open", "https://en.wikinews.org/wiki/Main_Page"))
    print(exit_code)

def open_weather():
    exit_code=subprocess.Popen(("xdg-open", "https://openweathermap.org/"))
    print(exit_code)
