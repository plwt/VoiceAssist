import subprocess

#Paths for the different applications
paths = {
    "notepad": "mousepad",
    "calculator": "/bin/mate-calculator",
    "firefox": "/opt/DevEdition/firefox-bin",
    "thunderbird": "/opt/thunderbird/thunderbird-bin",
    "zoom": "/snap/bin/zoom-client",
    "files": "thunar",
}

#Open the note pad
def open_notepad():
    subprocess.Popen(paths["notepad"])

#Open the calculator
def open_calculator():
    subprocess.Popen(paths["calculator"])

#Open firefox
def open_firefox():
    subprocess.Popen(paths["firefox"])

#Open thunderbird
def open_thunderbird():
    subprocess.Popen(paths["thunderbird"])

#Open zoom
def open_zoom():
    subprocess.Popen(paths["zoom"])

#Open the file manager
def open_files():
    subprocess.Popen(paths["files"])

#Opens the shutdown menu
def end_session():
    endsession = subprocess.Popen("xfce4-session-logout")
    print(endsession)

#Opens the terminal
def open_terminal():
    openterminal = subprocess.Popen(
        ["exo-open", "--launch", "TerminalEmulator", "--working-directory=/home/"]
    )
    print(openterminal)
