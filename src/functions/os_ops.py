import subprocess

#Paths for the different applications
paths = {
    "notepad": "mousepad",
    "calculator": "/bin/mate-calculator",
    "firefox": "/opt/DevEdition/firefox-bin",
    "thunderbird": "/opt/thunderbird/thunderbird-bin",
    "zoom": "/snap/bin/zoom-client",
    "files": "thunar",
    "code": "code",
    "volume": "alsamixer",
    "mute": "amixer set Master mute",
    "unmute": "amixer set Master unmute",
    "closezoom": "killall zoom",
    "graphics": "gimp",
    "closegraphics": "killall gimp",
    "closecalculator": "killall mate-calc",
    "closecode": "killall code",
    "lockscreen": "xdg-screensaver lock",
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

#Opens the code editor
def open_code():
    subprocess.Popen(paths["code"])

#Opens the volume control
def open_volume():
    subprocess.Popen(paths["volume"])

#Mutes the volume
def mute_volume():
    subprocess.Popen(paths["mute"])

#Unmutes the volume
def unmute_volume():
    subprocess.Popen(paths["unmute"])

#Closes Zoom
def close_zoom():
    subprocess.Popen(paths["closezoom"])
    
#Opens GIMP
def open_graphics():
    subprocess.Popen(paths["graphics"])
    
#Closes GIMP
def close_graphics():
    subprocess.Popen(paths["closegraphics"])
    
#Closes calculator
def close_calculator():
    subprocess.Popen(paths["closecalculator"])

#Closes the code editor
def close_code():
    subprocess.Popen(paths["closecode"])
    
#Locks screen
def lock_screen():
    subprocess.Popen(paths["lockscreen"])

