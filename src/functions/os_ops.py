import subprocess
import datetime
import webbrowser

#Paths for the different applications
paths = {
    "notepad": "mousepad",
    "files": "thunar",
    "lockscreen": "/opt/VoiceAssist/src/functions/lockscreen.sh",
    "screenshot": "/opt/VoiceAssist/src/functions/screenshot.sh",
}

def open_notepad():
    # Open the note pad
    subprocess.Popen(paths["notepad"])

def close_notepad():
    # Closes the note pad
    subprocess.Popen(["killall", "mousepad"])

def open_firefox():
    # Open firefox
    subprocess.Popen(["firefox"])

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
    print(openterminal)a

def mute_volume():
    # Mutes the volume
    mutevolume = subprocess.Popen(
        ["amixer", "set", "Master", "mute"]
    )
    print(mutevolume)

def unmute_volume():
    # Unmutes the volume
    unmutevolume = subprocess.Popen(
        ["amixer", "set", "Master", "unmute"]
    )
    print(unmutevolume)
         
def lock_screen():
    # Locks screen
    subprocess.Popen(paths["lockscreen"])

def screen_shot():
    # Takes screen shot and saves file
    subprocess.Popen(paths["screenshot"])
    
def new_mail():
    # Opens Thunderbird new email
    subprocess.Popen(["/usr/lib/thunderbird/thunderbird", "-compose"])

def address_book():
    # Opens Thunderbird address book
    subprocess.Popen(["/usr/lib/thunderbird/thunderbird", "-addressbook"])
