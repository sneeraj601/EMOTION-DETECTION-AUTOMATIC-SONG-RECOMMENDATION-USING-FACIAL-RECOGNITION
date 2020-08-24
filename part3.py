import os
import random
import sys
import threading
from playsound import playsound
import pyttsx3
from pygame import mixer
from tkinter import *

os.system("clear")
print("\n\n#####################################################")
print(" Inside Part3.py --> Playing the song")
print("Emotion Detected "+sys.argv[1])
print("#####################################################\n\n")



def talkToMe(audio):
    "speaks audio passed as argument"
    print("\n\n"+audio+"\n\n")
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def play_sound():
    talkToMe("Sir if you want to stop then click stop button")

    songs =[]
    qs = os.getcwd()+"/songs/"
    qs = qs+sys.argv[1]
	
    print(qs)
    for root,dirs,files in os.walk(qs):
        for file in files:
                print(root)
                file = os.path.join(root,file)
                songs.append(file)

    
    song = random.choice(songs)
    print(song)
    print("Playing the song:  ",song)
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

def interm():
    play_sound()
    turn_off()
  
def dispaygui():
	root1 = Tk()
	root1.title("Emotion Detection & Automatic song recommendation using Face Recognition")
	root1.geometry("800x500")
	filename = PhotoImage(file = "back4.png")
	background_label = Label(root1, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	s = "Emotion Detected "+sys.argv[1]
	row = Frame(root1)
	label1 = Label(row,  width = 100, text = s, font=("Times New Roman", 20),justify=CENTER, height=1, fg="blue")
	row.pack(side=TOP, fill=X, padx=5, pady=1)
	label1.pack()

	row = Frame(root1)
	label2 = Label(row,  width = 100, text = "Press Play to play a song", font=("Times New Roman", 20),justify=CENTER, height=1, fg="blue")
	row.pack(side=TOP, fill=X, padx=5, pady=0)
	label2.pack()

	b2 = Button(root1, text='Play',font=("Times New Roman", 15), command=root1.destroy)
	b2.pack(side=BOTTOM, padx=5, pady=50)

	root1.mainloop()	
def turn_off():
	root = Tk()
	root.title("Emotion Detection & Automatic song recommendation using Face Recognition")
	root.geometry("800x500")
	filename = PhotoImage(file = "back4.png")
	background_label = Label(root, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	row = Frame(root)
	label1 = Label(row,  width = 100, text = "Press stop to stop the song", font=("Times New Roman", 20),justify=CENTER, height=1, fg="blue")
	row.pack(side=TOP, fill=X, padx=5, pady=1)
	label1.pack()

	b2 = Button(root, text='Stop',font=("Times New Roman", 15), command=root.destroy)
	b2.pack(side=BOTTOM, padx=5, pady=80)
	
	root.mainloop()
	print('\n\n\nSong finished')	
    
   
    
if sys.argv[1]=="sad" or sys.argv[1]=="disgust" or sys.argv[1]=="fear" or sys.argv[1]=="angry":
    talkToMe("Sir you are not looking fine. Your well being is our prime concern, click play, it will cheer you up.")
    dispaygui()
    interm()
