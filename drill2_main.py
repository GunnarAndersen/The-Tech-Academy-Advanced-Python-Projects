#Python Version: 3.7.2


#Author: Gunnar Andersen

#Purpose: Python Drill for the tech academy, show that I know how to do stuff

#Tested OS: Windows 10




import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk

class ParentWindow(Frame):


    def __init__(self, master ,*args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        text = Text(root)
        self.master = master
        self.master.minsize(500,500)
        self.master.maxsize(500,500)
        self.master.title("Browse files")
        self.create_button() #runs my function that makes the button
        self.askdir()     

    def create_button(self):
        self.browse_button = tk.Button(self.master,width=12,height=20,text='Browse',command=filedialog.askdirectory)
        self.browse_button.grid(row=1,column=1, padx= (30,0),pady=(15,0))
        self.filename = filedialog.askdirectory
        self.txt_display = tk.Entry(self.master,text='This is where')
        self.txt_display.grid(row=6,column=6, padx= (30,0),pady=(15,0))
        


    def askdir(self):
        self.filename = filedialog.askdirectory()
        print (self.filename)
        self.lbl_stuff = tk.Label(self.master,text=self.filename)
        self.lbl_stuff.grid(row=5,column=5, padx= (30,0),pady=(15,0))

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
