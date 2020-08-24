from tkinter import *
import os
import subprocess


root = Tk()
root.title("Emotion Detection & Automatic song recommendation using Face Recognition")
root.geometry("1000x563")

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "emosic.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def proceed():
	root.destroy()
	root.quit()
	os.system("python part1.py")
	os.system("python part2.py")


bl = Button(root, text='Quit',font=("Times New Roman", 16), command=root.quit)
bl.pack(side=BOTTOM, padx=5, pady=1)


bl = Button(root, text='Start',font=("Times New Roman", 16), command=proceed)
bl.pack(side=BOTTOM, padx=5, pady=5)




root.mainloop()
