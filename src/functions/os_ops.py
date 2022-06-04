import subprocess

paths = {
    'notepad': "mousepad",
    'calculator': "/bin/mate-calculator",
    'firefox': "/opt/DevEdition/firefox-bin",
    'thunderbird': "/opt/thunderbird/thunderbird-bin",
    'zoom': "/snap/bin/zoom-client",
    'files': "thunar",
}

def open_notepad():
    subprocess.Popen(paths['notepad'])

def open_calculator():
    subprocess.Popen(paths['calculator'])

def open_firefox():
    subprocess.Popen(paths['firefox'])

def open_thunderbird():
    subprocess.Popen(paths['thunderbird'])
  
def open_zoom():
    subprocess.Popen(paths['zoom'])

def open_files():
    subprocess.Popen(paths['files'])
    
def end_session():
    endsession = subprocess.Popen("xfce4-session-logout")
    print(endsession)

def open_terminal():
    openterminal=subprocess.Popen(["exo-open", "--launch", "TerminalEmulator", "--working-directory=/home/"])
    print(openterminal)
