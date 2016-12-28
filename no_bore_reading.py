import os
import time
import pyperclip
time.sleep(2)
os.system("xdotool key --delay 13 ctrl+c")
x=pyperclip.paste()
f=open("/tmp/temp", "w")
length = f.write(x)
f.close()
time.sleep(1)
os.system("espeak -f /tmp/temp")

