#Imports 
from tkinter import *
import tkinter as tk
from Install.install import *
from Admin.Home import HomePage
import time as t
from Install.install import run,threadreq
from Database.utils import threadentries


#=======================================================MainPage====================================================
class MainPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Installation')
        self.master.geometry("1000x550")
        self.master.configure(bg='grey50')
        self.master.resizable(0,0)
        #mainframe
        self.frame1 = tk.Frame(master, bg="grey50")

        # Child frame
        self.frame0 = tk.Frame(self.frame1, highlightbackground="#242C35", highlightthickness=3,bg='grey50', width = 600)

        #Text To Display
        t = "Welcome to GAIS "
        t_1 = "This project is about."

        # Child frame contains
        self.lab0 = tk.Label(self.frame0, bg="grey50",text= t,font=("Helvetica",20,'bold'), fg='white')
        self.frame01 = tk.Frame(self.frame0, bg='#242C35', height = 10, width = 500)
        self.lab01 = tk.Label(self.frame0,bg = 'grey50',text= t_1,font=("Helvetica",16,'bold'), fg='white')

        #install button (will tigger python exe installion and requirement installation)
        self.button1 = tk.Button(self.frame1, text='INSTALL',bg="#242C35",height=5, width=30,font=("Helvetica",12,'bold'), fg='white',
                                 command=lambda: [install(), self.new_window(),self.press()])
        
        # frame Alignment
        self.lab0.place(relx=.5, rely=.3, anchor=CENTER)
        self.frame01.place(relx=.3, rely=.35, anchor=CENTER)
        self.lab01.place(relx=.5, rely=.4, anchor=CENTER)

        self.frame0.pack(side = LEFT, expand = True, fill= BOTH)
        self.button1.pack(side = LEFT, anchor = CENTER , padx= 100, pady= 30)

        self.frame1.pack(side = LEFT,expand = True,fill= BOTH)

    # Function to Show HomePage
    def new_window(self):
        newWindow = tk.Toplevel(self.master)
        Thread(target = lambda :[threadreq(),threadentries(),HomePage(newWindow),run()]).start()
        # app = HomePage(newWindow)
        # newWindow.state('zoomed')

    
    def press(self):
        t.sleep(5)
        self.lab02 = tk.Label(self.frame1,bg = 'grey50',text= 'INSTALLED',font=("Helvetica",16,'bold'), fg='white')
        self.lab02.place(relx=.8, rely=.7, anchor=CENTER)
#=================================================================End=====================================================================
        

