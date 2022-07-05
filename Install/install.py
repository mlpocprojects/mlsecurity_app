# Imports
from tkinter import *
import os
import sys
import webbrowser
from threading import Thread
   
# install function which will install python exe
def install():
    print("PYTHON VERSION CHECK--------------")
    print(sys.version_info[1])
    if str(sys.version_info[0]) != '3' or str(sys.version_info[1]) <= '6':
        print("Need 3.6 python")
        link = 'https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe'
        webbrowser.open(link, new=0)
    print("PYTHON VERSION CORRECT")

# requirement installation
def requirements():
        try:
            os.system('cmd /k "pip install -r MlSecurity/requirements.txt"')
        except:
            os.system('cmd /k "pip3 install -r MlSecurity/requirements.txt"')
        print("Requirements installed")

def threadreq():
        t2 = Thread(target=requirements)
        t2.start()

# run Project file
def run():
    print("Running Program")
    os.system("python MlSecurity/Runner.py")

# def exit_win():
#     os.system("kill -9 %d"%(os.getppid()))
#     os._exit(-1)
#     os._exit()
#     import subprocess
#     import sys

#     subprocess.Popen(["mupdf", "/home/dan/Desktop/Sieve-JFP.pdf"])
#     sys.exit(0)