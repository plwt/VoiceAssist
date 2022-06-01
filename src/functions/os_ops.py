import os
import subprocess as sp

paths = {
    'notepad': "mousepad",
    'calculator': "/bin/mate-calculator",
    'firefox': "/opt/DevEdition/firefox-bin",
    'thunderbird': "/opt/thunderbird/thunderbird-bin",
    'zoom': "/snap/bin/zoom-client",
    'files': "thunar",
    'terminal': "/bin/xfce4-terminal"
    'shutdown': "xfce4-session-logout"
    

}


def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_firefox():
    sp.Popen(paths['firefox'])

def open_thunderbird():
    sp.Popen(paths['thunderbird'])

def open_terminal():
    sp.Popen(paths['terminal'])

def open_zoom():
    sp.Popen(paths['zoom'])

def open_files():
    sp.Popen(paths['files'])

def open_zoom():
    sp.Popen(paths['zoom'])
    
def shutdown():
    sp.Popen(paths['shutdown'])
