# Imports 
from logging import root
from tkinter import *
import tkinter as tk
import os
import webbrowser
import validators
import time as t
import cv2
from threading import Thread
from PIL import Image, ImageTk
import socket


#================================================CameraPage=====================================================
class CameraPage:
    # Press Function execute when clicked on camera show all camera Management 
    # which include (close , camera link, stop, test camera)  
    def __init__(self,master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.configure(bg='grey50')
        self.master.title('camera_testing')
        #Reading camera 
        self.cap = cv2.VideoCapture(0)

        global camera
        camera = tk.StringVar()
        global cam_on
        cam_on = False

        # self.frame3 = tk.Frame(self.master, highlightbackground="#242C35", highlightthickness=3,bg='grey50')

        self.lab2 = tk.Label(self.master, bg="#242C35",text="CAMERA URL",height=3, width=15,font=("Helvetica",10,'bold'), fg='white')

        # self.cameraButton.configure(command=self.hide_me(self.cameraButton))
        # camera entry
        camera = tk.Entry(self.master, textvariable=camera, width=15,font=("Helvetica",34))

        # Test Camera button
        self.TestButton = tk.Button(self.master, bg="#242C35",text="TEST CAMERA",font=("Helvetica",10,'bold'),
                                    height=3, fg='white', width=15, command = lambda : [self.start_vid()])
        
        # stop camera button
        self.stop = tk.Button(self.master, bg="#242C35",text="STOP", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=self.stop_vid)

        # Child Frame alignment
        self.display1 = tk.Label(self.master, bg="#242C35")
        self.lab2.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)
        camera.pack(side =LEFT, anchor = NW,padx=1, pady=10, expand = True)
        self.TestButton.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)
        self.stop.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)

        self.display1.place(relx=.5, rely=.57, height = 500, width = 500, anchor="center")
        # self.frame3.place(relx=.5, rely=.5, anchor="center", height = 600 , width = 1100)
       
    # Function to show camera frame while checking camera link is valid or not
    def show_frame(self):
        try:
            if validators.url(camera.get()):
                if cam_on:
                    ret, frame = self.cap.read()
                    if ret:
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        img = Image.fromarray(cv2image).resize((480, 480))
                        imgtk = ImageTk.PhotoImage(image=img)
                        self.display1.imgtk = imgtk
                        self.display1.configure(image=imgtk)
        except:
            print("wrong")
        try:
            ret, frame = self.cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image).resize((480, 480))
                imgtk = ImageTk.PhotoImage(image=img)
                self.display1.imgtk = imgtk
                self.display1.configure(image=imgtk)
        except:
            print("wrong")
        self.display1.after(1, self.show_frame)

    # Start video frames
    def start_vid(self):
        global cam_on
        cam_on = True
        self.show_frame()

    # stop video frames
    def stop_vid(self):
        global cam_on
        cam_on = False
        if self.cap:
            self.cap.release()
            self.display1.config(image="")

    # destroy window 
    def close_windows(self):
        self.master.destroy()
#==================================================================End==================================================
def main():
    root = tk.Tk()
    app = CameraPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()