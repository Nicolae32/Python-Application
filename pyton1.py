
# import required module 
# I like to do stuff like this
import pyttsx3
import AppOpener
import os
from AppOpener import open
# driver code

# create object and assign voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# changing index changes voices but only
# 0 and 1 are working here
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")
print("")

# introduction
print(" =============================================== Hello World!! ================================================")
engine.say('Hello World!!')

print("")

print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER	 \t 6.ADOBE ILLUSTRATOR \n\t 7.ADOBE PHOTOSHOP \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD	 \t 10.TELEGRAM \n\n\t\t	 0. FOR EXIT")

print("\n	 (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")

print("\n ============================================ Welcome To My Tools ============================================")
pyttsx3.speak("Welcome to my tools")
print("")
print("")

pyttsx3.speak("chat with me with your requirements")

while True:
	# take input
	print(" CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
	p = input()
	p = p.upper()
	print(p)

	if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
		pyttsx3.speak("Type Again")
		print(".")
		print(".")
		continue

	# assignments for different applications in the menu

	elif ("4" in p):
		pyttsx3.speak("Opening")
		pyttsx3.speak("GOOGLE")
		print(".")
		print(".")
		open("thorium") #This one works only on my PC! (Change it to your browser name)

	elif ("8" in p):
		pyttsx3.speak("Opening")
		pyttsx3.speak("MICROSOFT EDGE")
		print(".")
		print(".")
		os.system("msedge")

	elif ("9" in p):
		pyttsx3.speak("Opening")
		pyttsx3.speak("NOTEPAD")
		print(".")
		print(".")
		os.system("Notepad")

	# close the program
	elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
		pyttsx3.speak("Exiting")
		break

	# for invalid input
	else:
		pyttsx3.speak(p)
		print("Is Invalid,Please Try Again")
		pyttsx3.speak("is Invalid,Please try again")
		print(".")
		print(".")
