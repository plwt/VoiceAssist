import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    # 'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
    'firefox': "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    'thunderbird': "C:\\Program Files\\Mozilla Thunderbird\\thunderbird.exe"
    'zoom': "C:\\Program Files\\Zoom\\Zoom.exe"
    'files': "C:\\Users\\ashut\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\AutomaticDestinations"

}


def open_notepad():
    os.startfile(paths['notepad'])


# def open_discord():
#     os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
