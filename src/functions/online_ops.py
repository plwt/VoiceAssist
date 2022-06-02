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
    exit_news = sp.call('/opt/VoiceAssist/src/functions/news.sh')
    print(exit_news)

def open_weather():
    exit_weather = sp.call('/opt/VoiceAssist/src/functions/weather.sh')
    print(exit_weather)