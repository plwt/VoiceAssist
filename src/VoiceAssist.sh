#!/bin/bash

cd /opt/VoiceAssist;history -d $(history 1)

chmod +x /opt/VoiceAssist/src/functions/screenshot.sh;history -d $(history 1)
chmod +x /opt/VoiceAssist/src/functions/lockscreen.sh;history -d $(history 1)


python3 -m venv venv;history -d $(history 1)
source venv/bin/activate;history -d $(history 1)

# install requirements in venv
python3 -m pip install --upgrade pip;history -d $(history 1)
python3 -m pip install --upgrade datetime;history -d $(history 1)
python3 -m pip install --upgrade python-decouple;history -d $(history 1)
python3 -m pip install --upgrade PyAudio;history -d $(history 1)
python3 -m pip install --upgrade requests;history -d $(history 1)
python3 -m pip install --upgrade pywhatkit;history -d $(history 1)
python3 -m pip install --upgrade pyttsx3;history -d $(history 1)
python3 -m pip install --upgrade SpeechRecognition;history -d $(history 1)

# run the script
python3 /opt/VoiceAssist/src/main.py;history -d $(history 1)

sleep 1m;history -d $(history 1)

deactivate;history -d $(history 1)

rm -r venv;history -d $(history 1)
