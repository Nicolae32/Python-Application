
# import required module 
# I like to do stuff like this
import pyttsx3
import AppOpener
import os
from AppOpener import open

 # create object and assign voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# changing index changes voices but only
# 0 and 1 are working here
engine.setProperty('voice', voices[0].id)
engine.runAndWait()
print("")
print("")

pyttsx3.speak("chat with me with your requirements")

while True:
	# take input
	print("App that you want to open: ", end='')
	
	p = input()
	p = p.upper()
	print(p)

	open(p)
	pyttsx3.speak("Opening")
	
	# close the program
	if ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
	
		pyttsx3.speak("Exiting")
	
		break

	