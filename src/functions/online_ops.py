import requests
import pywhatkit as kit
import smtplib
from decouple import config
import subprocess as sp


def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def open_news():
    exit_code=sp.Popen(("xdg-open", "https://en.wikinews.org/wiki/Main_Page"))
    print(exit_code)

def open_weather():
    exit_code=sp.Popen(("xdg-open", "https://openweathermap.org/"))
    print(exit_code)
