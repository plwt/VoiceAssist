#!/bin/bash

cd /opt/DAVE

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade datetime
python3 -m pip install --upgrade python-decouple
python3 -m pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

# run the script
python3 /opt/DAVE/src/main.py

sleep 5m

deactivate

rm -r venv
