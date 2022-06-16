import subprocess

#Paths for the different applications
paths = {
    "notepad": "mousepad",
    "calculator": "/bin/mate-calculator",
    "closecalculator": "/opt/VoiceAssist/src/functions/closecalculator.sh",
    "firefox": "/opt/DevEdition/firefox-bin",
    "thunderbird": "/opt/thunderbird/thunderbird-bin",
    "zoom": "/snap/bin/zoom-client",
    "files": "thunar",
    "code": "/opt/VoiceAssist/src/functions/code.sh",
    "volume": "alsamixer",
    "mute": "/opt/VoiceAssist/src/functions/mute.sh",
    "unmute": "/opt/VoiceAssist/src/functions/unmute.sh",
    "graphics": "/opt/VoiceAssist/src/functions/graphics.sh",
    "lockscreen": "/opt/VoiceAssist/src/functions/lockscreen.sh",
    "office": "/opt/VoiceAssist/src/functions/office.sh",
    "screenshot": "/opt/VoiceAssist/src/functions/screenshot.sh",
}

def open_notepad():
    # Open the note pad
    subprocess.Popen(paths["notepad"])

def close_notepad():
    # Closes the note pad
    subprocess.Popen(["killall", "mousepad"])

def open_calculator():
    # Open the calculator
    subprocess.Popen(paths["calculator"])

def close_calculator():
    # Closes the calculator
    subprocess.Popen(["killall", "mate-calc"])
   
def open_firefox():
    # Open firefox
    subprocess.Popen(paths["firefox"])

def open_thunderbird():
    # Open thunderbird
    subprocess.Popen(paths["thunderbird"])

def open_zoom():
    # Open zoom
    subprocess.Popen(paths["zoom"])

def close_zoom():
    # Closes zoom
    subprocess.Popen(["killall", "zoom"])

def open_files():
    # Open the file manager
    subprocess.Popen(paths["files"])

def close_files():
    # Closes the file manager
    subprocess.Popen(["killall", "Thunar"])

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

def close_code():
    # Closes the code editor
    subprocess.Popen(["killall", "code"])

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

def close_graphics():
    # Closes GIMP
    subprocess.Popen(["killall", "gimp"])
        
def lock_screen():
    # Locks screen
    subprocess.Popen(paths["lockscreen"])
    
def open_office():
    # Opens Libreoffice
    subprocess.Popen(paths["office"])
    
def screen_shot():
    # Takes screen shot and saves file
    subprocess.Popen(paths["screenshot"])
