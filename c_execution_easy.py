#inorder to make the program to work you need
# xdotool 
# pyperclip
# python ( ofcourse )
# important it is done for linux based system so windows user hit " powershell " that will give u necessary power 

import os
import time
import pyperclip #library for accessing clipboard

#creating a time delay for 2 seconds
time.sleep(2)

#sending the key stroke ctrl+c i.e copy using xdotool
os.system("xdotool key --delay 13 ctrl+c")

#some predefined stmt
x = "#include<stdio.h>\nint main(){"

#combine above stmt with what we copied
x+=pyperclip.paste()

#last touch to c code
x+="return 0;}"

#creating 1 sec delay
time.sleep(1)

# i prefare storing files in tmp directory 
f=open("/tmp/code.c","w")

#write the data to file and length contains no of bytes return if u want use it or leave it
length = f.write(x)

#close the file
f.close()

##  Here is the actual magic happens open a terminator with /tmp as working directory and compile then execute the c file

# one more thing why cat?  for suspend the process 

# not understand remove the cat and try ( terminal disappear rapidly ) so to stop that cat help u

os.system("terminator --working-directory=/tmp -e 'gcc -o code code.c;./code;cat'")

# if you have issue and doubts e-mail me or post comment 

# HAPPY PYTHON HUNTING
