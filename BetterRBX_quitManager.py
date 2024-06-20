import os
import keyboard
import time
import psutil

def is_process_running(process_name):
    """Check if there is any running process that contains the given name."""
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def change():
    if is_process_running("RobloxPlayerBeta"):
        os.system("taskkill /im RobloxPlayerBeta.exe /f")
    elif is_process_running("chrome"):
        os.system("taskkill /im chrome.exe /f")

keyboard.add_hotkey('ctrl+q', change)

while True:
    time.sleep(0.1)
