Better Roblox is a replacement (kind of) for the laggy Roblox desktop app. I found the web version of Roblox pretty good so I put it into Chrome kiosk and made a Py file to quit the kiosk and the Roblox app without entering the desktop version.

# Preparations
1. Install Chrome ( https://www.google.com/chrome/next-steps.html )
2. Install Python ( https://www.python.org/downloads/ )
3. Install keyboard and psutil ( run "pip install keyboard psutil" in the Py terminal)
   
# How to use 
It is very simple, just follow the instructions below!

## (Optional) Add Roblox Chrome extensions
Here are some examples:
Rogold - http://www.rogold.live                        
Ropro - http://www.ropro.io                        
BTRoblox - https://chromewebstore.google.com/detail/hbkpclpemjeibhioopcebchdmohaieln                             

## 1. Open Roblox Player Pro.py
To prevent entering the desktop app and to make it easier to  open and close the kiosk, I made a Python file that opens up Roblox in Chrome..
### Press ctrl+alt+y to quit Roblox/Chrome (If you close Chrome, you close the Python file so just reopen it to relaunch Roblox web.)
Note: It might take a couple of seconds for the program to close!

## (Optional) Customize the quit shortcut
To do it, open the Py file with VScode or any Python editor program. Go to line 19 (or the line that contains "keyboard.add_hotkey) and enter anything instead of 'ctrl+alt+y'.
### Make sure, that you don't delete the two >'<.

## (Optional) Add the Roblox Player Pro to startup
By doing this, you won't have to open the Py file all the time because it will automatically open when you turn on your computer.
To do this you need to press Win+r. This will open up run. Now you should type in "shell:startup" and hit enter. Now you have to copy Roblox Palyer Pro.py to the folder that it just opened.



