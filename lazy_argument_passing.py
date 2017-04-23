#passing many argument is time consuming and boring so to make it easy i created a python script

# Dependencies
#       xdotools for sending arguments to program
#       zenity for dialog box generation 

import os
import time

#os.system("zenity --title 'Lazy arguments' --entry --text 'Enter the arguments' > /tmp/lazy")

os.system("zenity --editable --title 'Lazy arguments' --text-info --text 'Enter the arguments' --height=500 --width=501 > /tmp/lazy")

time.sleep(1)

os.system("xdotool type --file /tmp/lazy")

#working

# pretty easy script 
# 1. get the arguments to be passed using zenity
# 2. send it using xdotools
