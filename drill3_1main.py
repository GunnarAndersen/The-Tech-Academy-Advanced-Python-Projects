#Python Version: 3.7.2


#Author: Gunnar Andersen

#Purpose: Python Drill for the tech academy, show that I know how to do stuff

#Tested OS: Windows 10


import os
import shutil
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import sqlite3
conn = sqlite3.connect('text_files.db')
file1 = 'Flex.txt'
file2 = 'Text.txt'



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
        self.insertSQL()
        self.insertShutil()
    def create_button(self):
        self.browse_button = tk.Button(self.master,width=12,height=20,text='Browse',command=filedialog.askdirectory)
        self.browse_button.grid(row=1,column=1, padx= (30,0),pady=(15,0))
        self.filename = filedialog.askdirectory
        self.txt_display = tk.Entry(self.master,text='This is where')
        self.txt_display.grid(row=6,column=6, padx= (30,0),pady=(15,0))
        
        

    def askdir(self):
        self.filename = filedialog.askdirectory()
        print (self.filename)
        self.file = filedialog.askopenfilename(initialdir = self.filename,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        self.file2 = filedialog.askopenfilename(initialdir = self.filename,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        print (self.file)
        print(self.file2)
        self.lbl_stuff = tk.Label(self.master,text=self.filename)
        self.lbl_stuff.grid(row=5,column=5, padx= (30,0),pady=(15,0))
        fPath = os.listdir(path=self.filename)
        print(fPath)
        fileList = tuple(fPath)
        print(fileList)
        
        fPath2 = 'C:\\drillFolder\\'
        jPath = os.path.join(self.filename, self.file) #FPATH doesn't work because it displays contents in the folder, so you need to be more specific in a way.
        print(jPath)
        tPath = os.path.getmtime(jPath)
        print(tPath)
        xPath = os.path.join(self.filename, self.file2)
        print(xPath)
        zPath = os.path.getmtime(xPath)
        print(zPath)
        


#Cole suggested to put like self,filename in this function
    def insertSQL(self):
                    
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_textfiles STR, \
                    col_timestamps INTEGER)")
            conn.commit()
            fPath = os.listdir(path=self.filename)
            fileList = tuple(fPath)
            with conn:
                cur.execute("INSERT INTO tbl_files(col_textfiles) VALUES(?)",(file2,))
                cur.execute("INSERT INTO tbl_files(col_textfiles) VALUES(?)",(file1,))
                for file in fileList:
                    if ".txt" in file:
                        print(file) #I should not print those values. I should print the paths- please remember after chess to do that.
                        #In retrospect I cannot but I can put in the getmtime and the text names in all at once'''
               
                

                
    def insertShutil(self):
        source = os.listdir("C:\\drillFolder\\")
        destination = "C:\\A\\"
        for files in source:
            if files.endswith(".txt"):
                shutil.move('C:\\drillFolder\Flex.txt','C:\\A\\')
                shutil.move('C:\\drillFolder\Text.txt','C:\\A\\')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
   
    
