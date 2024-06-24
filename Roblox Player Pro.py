import os
import keyboard
import time
import psutil
import subprocess

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
url = "http://web.roblox.com"
kiosk_mode = "--kiosk"

subprocess.Popen([chrome_path, kiosk_mode, url])

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def change():
    print("Hotkey pressed")
    if is_process_running("RobloxPlayerBeta"):
        os.system("taskkill /im RobloxPlayerBeta.exe /f")
    if is_process_running("chrome"):
        os.system("taskkill /im chrome.exe /f")
        time.sleep(1)
        os.system("taskkill /im python.exe /f")


keyboard.add_hotkey('ctrl+alt+y', change)

while True:
    time.sleep(0.1)

