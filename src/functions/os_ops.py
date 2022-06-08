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

#Mutes the volume
def mute_volume():
    mutevolume = subprocess.Popen(
        ["amixer", "set", "Master", "mute"]
    )
    print(mutevolume)

#Unmutes the volume
def unmute_volume():
    subprocess.Popen(paths["unmute"])
    
#Opens GIMP
def open_graphics():
    subprocess.Popen(paths["graphics"])
        
#Locks screen
def lock_screen():
    subprocess.Popen(paths["lockscreen"])
    
#Opens Libreoffice Calc
def open_spreadsheet():
    subprocesss.Popen(paths["spreadsheet"])
    
#Opens Libreoffice Writer
def open_writer():
    subprocess.Popen(paths["writer"])

#Takes screen shot and saves file
def screen_shot():
    subprocess.Popen(paths["screenshot"])
