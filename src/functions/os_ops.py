import os
import subprocess as sp

paths = {
    'notepad': "/bin/mousepad",
    # 'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "/bin/mate-calculator",
    'firefox': "/opt/DevEdition/firefox-bin",
    'thunderbird': "/opt/thunderbird/thunderbird-bin",
    'zoom': "/var/lib/snapd/desktop/applications/zoom-client_zoom-client.desktop /snap/bin/zoom-client",
    'files': "/bin/thunar ",
    'terminal': "/bin/xfce4-terminal"

}


def open_notepad():
    os.startfile(paths['notepad'])


# def open_discord():
#     os.startfile(paths['discord'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_firefox():
    sp.Popen(paths['firefox'])

def open_thunderbird():
    sp.Popen(paths['thunderbird'])

def open_terminal():
    sp.Popen(paths['terminal'])
    
# def open_camera():
#     sp.run('start microsoft.windows.camera:', shell=True)

def open_zoom():
    sp.Popen(paths['zoom'])

def open_files():
    sp.Popen(paths['files'])
