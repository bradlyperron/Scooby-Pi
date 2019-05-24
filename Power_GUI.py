import sys
from tkinter import *
import os

root = Tk()

def Speaker_on(): 
    os.system('python Speaker_on.py')
	
def Speaker_off(): 
	os.system('python Speaker_off.py')
	
def Phone_on():
	os.system('python Phone_on.py')
	
def Phone_off():
	os.system('python Phone_off.py')

def Modem_on():
	os.system('python Modem_on.py')
	
def Modem_off():
	os.system('python Modem_off.py')    
      
Label(root, text="Speaker").grid(row=0, column=0)
Radiobutton(root, text = "On", variable = 1, value = 0, command = Speaker_on).grid(row=0, column=2)
Radiobutton(root, text = "Off", variable = 1, value = 1, command = Speaker_off).grid(row=0, column=4)

Label(root, text="Phone").grid(row=2, column=0)
Radiobutton(root, text = "On", variable = 2, value = 0, command = Phone_on).grid(row=2, column=2)
Radiobutton(root, text = "Off", variable = 2, value = 1, command = Phone_off).grid(row=2, column=4)

Label(root, text="Modem").grid(row=4,column=0)
Radiobutton(root, text = "On", variable = 3, value = 0, command = Modem_on).grid(row=4, column=2)
Radiobutton(root, text = "Off", variable = 3, value = 1, command = Modem_off).grid(row=4, column=4)




root.mainloop()





