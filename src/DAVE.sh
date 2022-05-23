#!/bin/bash

cd /opt/DAVE

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade datetime
python3 -m pip install --upgrade python-decouple
python3 -m pip install --upgrade PyAudio
python3 -m pip install --upgrade requests
python3 -m pip install --upgrade pywhatkit
python3 -m pip install --upgrade pyttsx3
python3 -m pip install --upgrade SpeechRecognition

# run the script
python3 /opt/DAVE/src/main.py

sleep 5m

deactivate

rm -r venv
