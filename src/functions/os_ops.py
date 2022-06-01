import os
import subprocess as sp

paths = {
    'notepad': "mousepad",
    'calculator': "/bin/mate-calculator",
    'firefox': "/opt/DevEdition/firefox-bin",
    'thunderbird': "/opt/thunderbird/thunderbird-bin",
    'zoom': "/snap/bin/zoom-client",
    'files': "thunar",
    'terminal': "/bin/xfce4-terminal",
    'shutdown': "/bin/xfce4-session-logout"
    

}


def open_notepad():
    sp.Popen(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_firefox():
    sp.Popen(paths['firefox'])

def open_thunderbird():
    sp.Popen(paths['thunderbird'])

def open_terminal():
    # sp.Popen(paths['terminal'])
    os.system('cd')

def open_zoom():
    sp.Popen(paths['zoom'])

def open_files():
    sp.Popen(paths['files'])

def open_zoom():
    sp.Popen(paths['zoom'])
    
def end():
    sp.Popen(paths['shutdown'])
