# VoiceAssist

A voice assistant for Linux.  This has been designed for Debian 11 Xfce.  Please check the file paths in os_ops.py before use to make sure they are correct for your device.

Inspired by and forked from https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/ and https://www.codingthesmartway.com/python-and-chatgpt-4-develop-a-virtual-voice-assistant/

## Commands

| Say this... | to do this... 
| :-------------| :------------- 
| Open Files | Open Thunar file manager
| Close Files | Close all instances of Thunar file manager
| Open Notepad | Opens Mousepad
| Close Notepad | Close all instances of Mousepad
| Open Firefox | Opens Firefox
| Open Thunderbird | Opens Thunderbird
| Open Terminal | Opens Terminal
| End Session | Opens the log out options
| Quiet | Mutes speaker
| Loud | Unmutes speaker
| Open YouTube | User is asked for what they want to play on YouTube
| Search on Google | User is asked for what they want to search for using Google
| Open Maps | Opens openstreetmap.org in Firefox
| What is the news? | Opens wikinews.org in Firefox
| What is the weather? | Opens openweathermap.org in Firefox
| Take screen shot | Takes screenshot, saves it to desktop
| Lock screen | Locks screen 
| Exit | Stops VoiceAssist
| Time | Responds with current time
| New Mail | Opens new email client
| Address Book | Opens address book
| Computer (search term) | web search using Perplexity AI

Time is not yet tested

## Dependancies

sudo apt-get install python3-tk python3-dev python3.10-venv python3-pyaudio portaudio19-dev
