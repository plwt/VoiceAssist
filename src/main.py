from functions.online_ops import (
    # Online functions
    play_on_youtube,
    search_on_google,
    open_news,
    open_weather,
    open_maps,
    easter_egg,
)

from functions.os_ops import (
    # On device functions
    open_firefox,
    open_thunderbird,
    open_notepad,
    close_notepad,
    open_terminal,
    open_zoom,
    close_zoom,
    open_files,
    close_files,
    end_session,
    open_code,
    close_code,
    mute_volume,
    unmute_volume,
    lock_screen,
    screen_shot,

)
#Required for text to speach conversion
import pyttsx3

#Required for speach to text conversion
import speech_recognition as sr

#Required for date and time
from datetime import datetime

#Required for random responses
from random import choice

#"Working on it" type responses
from utils import opening_text

# from pprint import pprint
# import webbrowser
# from decouple import config
# import requests


# USERNAME = config('USER')
# BOTNAME = config('BOTNAME')

#Set up text to speech engine
engine = pyttsx3.init()

# Set Rate
engine.setProperty("rate", 190)

# Set Volume
engine.setProperty("volume", 1.0)

# Set Voice (Female)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[10].id)


def speak(text):
    # Used to speak whatever text is passed to it

    engine.say(text)
    engine.runAndWait()


def greet_user():
    # Greets the user according to the time

    hour = datetime.now().hour
    if (hour >= 1) and (hour < 12):
        speak(f"Good morning")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good evening")
        speak(f"How can I help you?")


def take_user_input():
    # Takes user input and converts it into text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-gb")
        if not "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night, take care!")
            else:
                speak("Have a good day!")
            exit()
    except Exception:
        speak(" ")
        query = "None"
    return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()

        if "open" in query and "notepad" in query:
            open_notepad()

        elif "close" in query and "notepad" in query:
            close_notepad()

        elif "open" in query and "terminal" in query:
            open_terminal()

        elif "open" in query and "firefox" in query:
            open_firefox()

        elif "open" in query and "thunderbird" in query:
            open_thunderbird()

        elif "open" in query and "zoom" in query:
            open_zoom()
        
        elif "close" in query and "zoom" in query:
            close_zoom()

        elif "open" in query and "files" in query:
            open_files()

        elif "close" in query and "files" in query:
            close_files()

        elif "open" in query and "youtube" in query:
            speak("What do you want to play on Youtube?")
            video = take_user_input().lower()
            play_on_youtube(video)

        elif "search on google" in query:
            speak("What do you want to search on Google?")
            query = take_user_input().lower()
            search_on_google(query)

        elif "news" in query:
            open_news()

        elif "weather" in query:
            open_weather()

        elif "end session" in query:
            end_session()

        elif "open" in query and "code" in query:
            open_code()

        elif "close" in query and "code" in query:
            close_code()

        elif "quiet" in query:
            mute_volume()
        
        elif "loud" in query:
            unmute_volume()
            
        elif "maps" in query:
            open_maps()
                            
        elif "lock screen" in query:
            lock_screen()
                       
        elif "screen" in query and "shot" in query:
            screen_shot()
            
         elif "My" in query and "voice" in query and "is" in query and "my" in query and "passport" in query and "verify" in query and "me" in query:
            easter_egg()
