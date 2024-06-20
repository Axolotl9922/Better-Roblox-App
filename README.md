Better Roblox is a replacement (kind of) for the laggy Roblox desktop app. I found the web version of Roblox pretty good so I put it into Chrome kiosk and made a Py file to quit the kiosk and the Roblox app without entering the desktop version.
# Preparations
1. Install Chrome ( https://www.google.com/chrome/next-steps.html )
2. Install Python ( https://www.python.org/downloads/ )
3. Install the keyboard package ( run "pip install keyboard" in the Py terminal)
   
# How to use 

## 1. Create the app shortcut
Go to your Desktop, right-click hit new, and then shortcut. For the location, enter the following:                                       
### "C:\Program Files\Google\Chrome\Application\chrome.exe" --kiosk "http://web.roblox.com.com"
(Note: if you don't want to use the kiosk version simply remove "--kiosk" from the text above!)
You can name it whatever you want but I recommend something like, "Alt Roblox Player" or "Roblox Player+"

## 2. Customize the shortcut icon
Right-click on the shortcut (It will look like Chrome) and select "Properties". Go to "Shortcut" and click "Change icon". Click "Browse" and select any .ICO files you want or just use the one I put into the replit.

## (Optional) Add Roblox Chrome extensions
Here are some examples:
Rogold - http://www.rogold.live                        
Ropro - http://www.ropro.io                        
BTRoblox - https://chromewebstore.google.com/detail/hbkpclpemjeibhioopcebchdmohaieln                             

## 3. Open the quit manager.
To prevent entering the desktop app and to make it easier to quit the kiosk, I made a Python file that quits Roblox and Chrome (when Roblox is not open).
### Press ctrl+q to quit Roblox/Chrome

## (Optional) Customize the quit shortcut
To do it, open the Py file with VScode or any Python editor program. Go to line 19 (or the line that contains "keyboard.add_hotkey) and enter anything instead of 'ctrl+q'.
### Make sure, that you don't delete the two >'<.

## (Optional) Add the quit manager to startup
By doing this, you won't have to open the Py file all the time because it will automatically open when you turn on your computer.
To do this you need to press Win+r. This will open up run. Now you should type in "shell:startup" and hit enter. Now you have to copy the betterRBX_quitManager.py file (what a good name) to the folder that it just opened.

# Activation
Simply open the Py file and then press open the chrome kiosk shortcut
(To exit the app, press the quit hotkey ("ctrl+q" by default) and it should close Roblox or Chrome. If Roblox is open, it will only close it and not Chrome.)


