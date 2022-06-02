from functions.online_ops import play_on_youtube, search_on_google, open_news, open_weather
from functions.os_ops import open_calculator, open_firefox, open_thunderbird, open_notepad, open_terminal, open_zoom, open_files, end_session
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from random import choice
from utils import opening_text
#from pprint import pprint
#import webbrowser
#from decouple import config
#import requests


# USERNAME = config('USER')
# BOTNAME = config('BOTNAME')


engine = pyttsx3.init()

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 1) and (hour < 12):
        speak(f"Good morning")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good evening")
        speak(f"How can I help you?")

# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-gb')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night, take care!")
            else:
                speak('Have a good day!')
            exit()
    except Exception:
        speak(' ')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open terminal' in query or 'open terminal' in query:
            open_terminal()

        elif 'open firefox' in query:
            open_firefox()

        elif 'open thunderbird' in query:
            open_thunderbird()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open zoom' in query:
            open_zoom()

        elif 'open files' in query:
            open_files()

        elif 'youtube' in query:
            speak('What do you want to play on Youtube?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'news' in query:
            open_news()

        elif 'weather' in query:
            open_weather()
          
        elif "end session" in query:
            end_session()