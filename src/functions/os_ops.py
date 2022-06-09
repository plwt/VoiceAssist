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
    "mute": "/opt/VoiceAssist/src/functions/mute.sh",
    "unmute": "/opt/VoiceAssist/src/functions/unmute.sh",
    "graphics": "gimp",
    "lockscreen": "xdg-screensaver lock",
    "spreadsheet": "libreoffice --calc",
    "writer": "libreoffice --writer",
    "screenshot": "/opt/VoiceAssist/src/functions/screenshot.sh",
}

def open_notepad():
    # Open the note pad
    subprocess.Popen(paths["notepad"])

def open_calculator():
    # Open the calculator
    subprocess.Popen(paths["calculator"])

def open_firefox():
    # Open firefox
    subprocess.Popen(paths["firefox"])

def open_thunderbird():
    # Open thunderbird
    subprocess.Popen(paths["thunderbird"])

def open_zoom():
    # Open zoom
    subprocess.Popen(paths["zoom"])

def open_files():
    # Open the file manager
    subprocess.Popen(paths["files"])

def end_session():
    # Opens the shutdown menu
    endsession = subprocess.Popen("xfce4-session-logout")
    print(endsession)

def open_terminal():
    # Opens the terminal
    openterminal = subprocess.Popen(
        ["exo-open", "--launch", "TerminalEmulator", "--working-directory=/home/"]
    )
    print(openterminal)

def open_code():
    # Opens the code editor
    subprocess.Popen(paths["code"])

def mute_volume():
    # Mutes the volume
    mutevolume = subprocess.Popen(
        ["amixer", "set", "Master", "mute"]
    )
    print(mutevolume)

def unmute_volume():
    # Unmutes the volume
    subprocess.Popen(paths["unmute"])
    
def open_graphics():
    # Opens GIMP
    subprocess.Popen(paths["graphics"])
        
def lock_screen():
    # Locks screen
    subprocess.Popen(paths["lockscreen"])
    
def open_spreadsheet():
    # Opens Libreoffice Calc
    subprocesss.Popen(paths["spreadsheet"])
    
def open_writer():
    # Opens Libreoffice Writer
    subprocess.Popen(paths["writer"])

def screen_shot():
    # Takes screen shot and saves file
    subprocess.Popen(paths["screenshot"])
