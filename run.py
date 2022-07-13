# import 
from importlib.resources import path
from tkinter import *
import tkinter as tk
import os
import sys

from Admin.Main import MainPage
from Admin.Home import HomePage
from Admin.User import UserPage
from threading import Thread
from Install.install import run,threadreq
from Database.utils import threadentries


'''
file to run MainPage, UserPage and Homepage
'''
# requirement should download 
def main():
    globa_path = os.path.join(os.getcwd() ,'python-3.6.6-amd64.exe')
    root = tk.Tk()
    if str(sys.version_info[0]) == '3' or str(sys.version_info[1]) >= '6':
        t0 = Thread(target = lambda :[threadentries(),HomePage(root)])#threadreq,run()
        t0.start()
        root.mainloop()
    else:
        app = MainPage(root)
        root.mainloop()

# def main():
#     root = tk.Tk()
#     app = MainPage(root)
#     root.mainloop()

# def main():
#     root = tk.Tk()
#     app = UserPage(root,path=os.path.join(os.getcwd(), 'FaceRecog', 'images'))
#     root.mainloop()

if __name__ == '__main__':
    main()