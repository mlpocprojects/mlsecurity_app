# import 
from tkinter import *
import tkinter as tk
import os
import sys

from MainPage import MainPage
from HomePage import HomePage

'''
file to run MainPage, UserPage and Homepage
'''
# def main():
#     globa_path = os.path.join(os.getcwd() ,'python-3.6.6-amd64.exe')
#     root = tk.Tk()
#     if os.path.exists(globa_path) == True:
#         app = HomePage(root)
#         root.state('zoomed')
#         root.mainloop()
#     elif str(sys.version_info[0]) == '3' or str(sys.version_info[1]) >= '6':
#         app = HomePage(root)
#         root.state('zoomed')
#         root.mainloop()
#     else:
#         app = MainPage(root)
#         root.state('zoomed')
#         root.mainloop()

def main():
    root = tk.Tk()
    app = MainPage(root)
    root.state('zoomed')
    root.mainloop()

if __name__ == '__main__':
    main()