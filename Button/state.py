from tkinter import *

# Changing button state 
def changeState(x, y, z):
    if (x['state'] == NORMAL):
        y['state'] = NORMAL
        z['state'] = NORMAL