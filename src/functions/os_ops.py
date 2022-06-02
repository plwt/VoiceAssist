import os
import subprocess as sp

paths = {
    'notepad': "mousepad",
    'calculator': "/bin/mate-calculator",
    'firefox': "/opt/DevEdition/firefox-bin",
    'thunderbird': "/opt/thunderbird/thunderbird-bin",
    'zoom': "/snap/bin/zoom-client",
    'files': "thunar",
        
}

def open_notepad():
    sp.Popen(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_firefox():
    sp.Popen(paths['firefox'])

def open_thunderbird():
    sp.Popen(paths['thunderbird'])
  
def open_zoom():
    sp.Popen(paths['zoom'])

def open_files():
    sp.Popen(paths['files'])
    
def end_session():
    exit_code = sp.call('/opt/VoiceAssist/src/functions/endsession.sh')
    print(exit_code)

def open_terminal():
    exit_code = sp.call('/opt/VoiceAssist/src/functions/terminal.sh')
    print(exit_code)
