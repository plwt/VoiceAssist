# VoiceAssist

### Notes 

- Read the tutorial series - https://ireadblog.com/series/18/virtual-personal-assistant-using-python
- freeCodeCamp article: https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/
- Demo Video: https://vimeo.com/650156113
- sapi5 replacement for Linux - https://github.com/nateshmbhat/pyttsx3/issues/212
- Speach engine settings - https://cs.github.com/?scopeName=All+repos&scope=&q=engine+%3D+pyttsx3.init%28
- Portaudio install - https://stackoverflow.com/questions/35708238/installing-pyaudio-with-pip-in-a-virtualenv and https://stackoverflow.com/questions/50457197/pyaudio-installation-failure-on-ubuntu
- Voice options https://linuxhint.com/command-line-text-speech-apps-linux/ and https://levelup.gitconnected.com/make-your-python-program-speak-310766534fbf and https://scriptverse.academy/tutorials/python-text-to-speech.html
- pyttsx3 options https://pyttsx3.readthedocs.io/en/latest/engine.html#changing-voices
- Opening applications - https://stackoverflow.com/questions/51329742/how-to-write-a-python-script-to-open-applications-in-linux-mint

- Shutdown dialogue - https://askubuntu.com/questions/771166/how-can-i-safely-shut-down-xfce-from-the-terminal
- Possibly use this to open terminal at core folder location - https://stackoverflow.com/questions/71281841/use-subprocess-to-open-terminal-and-run-a-command



### Contents of .env file:

```
USER=None
BOTNAME=JARVIS
# EMAIL=None
# PASSWORD=None
# NEWS_API_KEY=None
# OPENWEATHER_APP_ID=None
# TMDB_API_KEY=None
```

### Requirements

```sudo apt-get install portaudio19-dev```

```sudo apt-get install python3-tk python3-dev```

```sudo apt update && sudo apt install espeak ffmpeg libespeak1```

### Commands

- Open notepad
- Open Firefox
- Open Thunderbird
- Open files
- Open Zoom
- Open calculator
- Open YouTube (follow up question)
- Search on Google (follow up question)
- Open terminal


- What is the news? (does not work)
- What is the weather? (does not work)
- End session (does not work)

## To Do

1. open terminal in default location
2. add full code comments
3. Add install requirements to .sh
4. Make a clean up .sh
