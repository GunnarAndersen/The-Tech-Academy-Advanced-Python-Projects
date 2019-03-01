from tkinter import *
import tkinter as tk
import os




class ParentWindow(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master #This makes it so that I don't have to write ParentWindow(Frame)
        self.master.minsize(500,500) #Height, width
        self.master.maxsize(500,500) # Height, width. This cannot be changed
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
                             
        arg = self.master


        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        
