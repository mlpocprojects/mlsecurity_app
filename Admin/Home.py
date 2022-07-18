# Imports 
from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import webbrowser
from requests import delete
import validators
import time as t
import cv2
from threading import Thread
from PIL import Image, ImageTk
from Button.state import changeState
from Admin.User import UserPage
import socket
from Database.utils import *
from Install.install import run
# from Admin.HomeD import HomePageD



#================================================HomePage=====================================================
class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("850x150")
        self.master.configure(bg='grey50')
        self.master.title('camera_testing')
        self.master.resizable(0,0)

        #Reading camera 
        self.cap = None

        #Main frame 
        self.frame2 = tk.Frame(self.master, bg='grey50')
        self.button_border = tk.Frame(self.frame2, highlightbackground="black",highlightthickness=2, bd=0)

        # User button for User-Management
        self.user = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='USER MANAGEMENT',font=("Helvetica",12,'bold'),
                              command=lambda: [self.new_window()], state=DISABLED, fg='white')
        #Start button to run Project                          
        self.start = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='START VERIFICATION',font=("Helvetica",12,'bold'), 
                                command= lambda : [self.threadlink(),self.new_window_1()], state=DISABLED, fg='white')#self.threadlink(),self.new_window_1()
        #Camera button for camera management 
        self.cameraButton = tk.Button(self.frame2, bg="#242C35", height=3, width=20, text="CAMERA MANAGEMENT",font=("Helvetica",12,'bold'),
                                      command=lambda: [self.press(),
                                                       changeState(self.cameraButton, self.user, self.start)],
                                      state=NORMAL, fg='white')

        # Frame and button alignment
        self.user.pack(side =LEFT, anchor = NW,padx=30, pady=30, expand = True)
        self.start.pack(side = LEFT, expand = True, anchor = N,padx=30, pady=30)
        self.cameraButton.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        self.frame2.pack(fill="both", expand=True)

    # function to pop up Browser 
    def link(self):
        t.sleep(15)
        hostname = "".join(("//", socket.gethostbyname(socket.gethostname()))) 
        links = ":".join(("http",hostname,"8880"))
        webbrowser.open_new(links)
        
    # Threading link function    
    def threadlink(self):
        t1 = Thread(target=self.link)
        t1.start()

    # hide camera frame 
    def hide_me(self, x):
        x.pack_forget()

    # Retrieve camera frame  
    def retrieve(self, x,z,*y):
        z.place_forget()
        x.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        for i in y:
            i.grid_forget()
        self.master.state('normal')

            
    # Press Function execute when clicked on camera show all camera Management 
    # which include (close , camera link, stop, test camera)  
    def press(self):
        global camera
        camera = tk.StringVar()
        global cam_on
        cam_on = False
        self.master.state('zoomed')

        self.frame3 = tk.Frame(self.frame2, highlightbackground="#242C35", highlightthickness=3,bg='grey50')

        self.lab2 = tk.Label(self.frame3, bg="#242C35",text="CAMERA URL",height=3, width=15,font=("Helvetica",10,'bold'), fg='white')

        # self.cameraButton.configure(command=self.hide_me(self.cameraButton))
        # camera entry
        camera = tk.Entry(self.frame3, textvariable=camera, width=10,font=("Helvetica",32,'bold'))

        # Test Camera button
        self.TestButton = tk.Button(self.frame3, bg="#242C35",text="TEST CAMERA",font=("Helvetica",10,'bold'),
                                    height=3, fg='white', width=15, command = lambda : [self.start_vid()])
        
        # stop camera button
        self.stop = tk.Button(self.frame3, bg="#242C35",text="STOP CAMERA", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=self.stop_vid)

        # close camera button 
        self.close = tk.Button(self.frame3,bg="#242C35", text="CLOSE CAMERA",font=("Helvetica",10,'bold'),height=3, width=15, fg='white',
                        command=lambda: [self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.stop_vid()])
        
        # Save camera Button
        self.Save = tk.Button(self.frame3, bg="#242C35",text="SAVE URL", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=lambda :[self.save_url(),self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.press()])
        
        self.delete = tk.Button(self.frame3, bg="#242C35",text="DELETE URL", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=lambda :[self.delete_url(),self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.press()])

        c_values = []
        get_list(mydb,f"SELECT * FROM {camera_db}", c_values)
        self.drop = ttk.Combobox(self.frame3, values = c_values,font=("Helvetica",20,'bold'))

        # Child Frame alignment
        self.display1 = tk.Label(self.frame3, bg="#242C35")
        self.lab2.pack(side =LEFT, anchor = NW,padx=10, pady=10, expand = True)
        camera.pack(side =LEFT, anchor = NW, pady=10, expand = True)
        self.Save.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.TestButton.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.stop.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.close.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)

        self.drop.place(relx=.14, rely=.3, anchor="center",height = 50, width = 250)
        self.delete.place(relx=.14, rely=.4, anchor="center",height = 50, width = 250)


        self.display1.place(relx=.5, rely=.57, height = 500, width = 500, anchor="center")
        self.frame3.place(relx=.5, rely=.57, anchor="center", height = 600 , width = 1100)

    def delete_url(self):
        url = self.drop.get()
        executor(mydb, f"Delete from {camera_db} where camera_url='{url}'")

    
    #To save camera url to database
    def save_url(self):
        try:
            s_camera = camera.get()
            executor(mydb,f"Insert into {camera_db} values('{s_camera}')")
        except :
            print("Already Exist")
       
    # Function to show camera frame while checking camera link is valid or not
    def show_frame(self):
        try:
            if validators.url(self.drop.focus()):
                if cam_on:
                    ret, frame = self.cap.read()
                    if ret:
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        img = Image.fromarray(cv2image).resize((480, 480))
                        imgtk = ImageTk.PhotoImage(image=img)
                        self.display1.imgtk = imgtk
                        self.display1.configure(image=imgtk)
                        self.display1.after(1, self.show_frame)
        except:
            print("wrong")
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
                        self.display1.after(1, self.show_frame)
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
                self.display1.after(1, self.show_frame)
        except:
            print("wrong")     

    # Start video frames
    def start_vid(self):
        global cam_on
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        cam_on = True
        self.show_frame()

    # stop video frames
    def stop_vid(self):
        global cam_on
        cam_on = False
        if self.cap:
            self.cap.release()
            self.display1.config(image="")
            
    # function to open User Management 
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserPage(self.newWindow, path=os.path.join(os.getcwd(), 'FaceRecog', 'images'))

    def new_window_1(self):
        self.master.destroy()
        root = tk.Tk()
        Thread(target = lambda :[HomePageD(root),run()]).start()
        root.mainloop()

    # destroy window 
    def close_windows(self):
        self.master.destroy()
#==================================================================End==================================================


#================================================HomePageD=====================================================
class HomePageD:
    def __init__(self, master):
        self.master = master
        self.master.geometry("850x150")
        self.master.configure(bg='grey50')
        self.master.title('camera_testing')
        self.master.resizable(0,0)

        #Reading camera 
        self.cap = None

        #Main frame 
        self.frame2 = tk.Frame(self.master, bg='grey50')
        self.button_border = tk.Frame(self.frame2, highlightbackground="black",highlightthickness=2, bd=0)

        # User button for User-Management
        self.user = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='USER MANAGEMENT',font=("Helvetica",12,'bold'),
                              command=lambda: [self.new_window()], state=NORMAL, fg='white')
        #Start button to run Project                          
        self.start = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='START VERIFICATION',font=("Helvetica",12,'bold'), 
                                command= lambda : [self.threadlink(),self.new_window_1()], state=NORMAL, fg='white')#self.threadlink()
        #Camera button for camera management 
        self.cameraButton = tk.Button(self.frame2, bg="#242C35", height=3, width=20, text="CAMERA MANAGEMENT",font=("Helvetica",12,'bold'),
                                      command=lambda: [self.press(),
                                                       changeState(self.cameraButton, self.user, self.start)],
                                      state=NORMAL, fg='white')

        # Frame and button alignment
        self.user.pack(side =LEFT, anchor = NW,padx=30, pady=30, expand = True)
        self.start.pack(side = LEFT, expand = True, anchor = N,padx=30, pady=30)
        self.cameraButton.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        self.frame2.pack(fill="both", expand=True)

    # function to pop up Browser 
    def link(self):
        t.sleep(3)
        hostname = "".join(("//", socket.gethostbyname(socket.gethostname()))) 
        links = ":".join(("http",hostname,"8880"))
        webbrowser.open_new(links)
        
    # Threading link function    
    def threadlink(self):
        t1 = Thread(target=self.link)
        t1.start()

    # hide camera frame 
    def hide_me(self, x):
        x.pack_forget()

    # Retrieve camera frame  
    def retrieve(self, x,z,*y):
        z.place_forget()
        x.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        for i in y:
            i.grid_forget()
        self.master.state('normal')

            
    # Press Function execute when clicked on camera show all camera Management 
    # which include (close , camera link, stop, test camera)  
    def press(self):
        global camera
        camera = tk.StringVar()
        global cam_on
        cam_on = False
        self.master.state('zoomed')

        self.frame3 = tk.Frame(self.frame2, highlightbackground="#242C35", highlightthickness=3,bg='grey50')

        self.lab2 = tk.Label(self.frame3, bg="#242C35",text="CAMERA URL",height=3, width=15,font=("Helvetica",10,'bold'), fg='white')

        # self.cameraButton.configure(command=self.hide_me(self.cameraButton))
        # camera entry
        camera = tk.Entry(self.frame3, textvariable=camera, width=10,font=("Helvetica",32,'bold'))

        # Test Camera button
        self.TestButton = tk.Button(self.frame3, bg="#242C35",text="TEST CAMERA",font=("Helvetica",10,'bold'),
                                    height=3, fg='white', width=15, command = lambda : [self.start_vid()])
        
        # stop camera button
        self.stop = tk.Button(self.frame3, bg="#242C35",text="STOP CAMERA", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=self.stop_vid)

        # close camera button 
        self.close = tk.Button(self.frame3,bg="#242C35", text="CLOSE CAMERA",font=("Helvetica",10,'bold'),height=3, width=15, fg='white',
                        command=lambda: [self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.stop_vid()])
        
        # Save camera Button
        self.Save = tk.Button(self.frame3, bg="#242C35",text="SAVE URL", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=lambda :[self.save_url(),self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.press()])
        
        self.delete = tk.Button(self.frame3, bg="#242C35",text="DELETE URL", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=lambda :[self.delete_url(),self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.press()])

        c_values = []
        get_list(mydb,f"SELECT * FROM {camera_db}", c_values)
        self.drop = ttk.Combobox(self.frame3, values = c_values,font=("Helvetica",20,'bold'))

        # Child Frame alignment
        self.display1 = tk.Label(self.frame3, bg="#242C35")
        self.lab2.pack(side =LEFT, anchor = NW,padx=10, pady=10, expand = True)
        camera.pack(side =LEFT, anchor = NW, pady=10, expand = True)
        self.Save.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.TestButton.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.stop.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)
        self.close.pack(side =LEFT, anchor = NW,padx=20, pady=10, expand = True)

        self.drop.place(relx=.14, rely=.3, anchor="center",height = 50, width = 250)
        self.delete.place(relx=.14, rely=.4, anchor="center",height = 50, width = 250)


        self.display1.place(relx=.5, rely=.57, height = 500, width = 500, anchor="center")
        self.frame3.place(relx=.5, rely=.57, anchor="center", height = 600 , width = 1100)

    def delete_url(self):
        url = self.drop.get()
        executor(mydb, f"Delete from {camera_db} where camera_url='{url}'")

    
    #To save camera url to database
    def save_url(self):
        try:
            s_camera = camera.get()
            executor(mydb,f"Insert into {camera_db} values('{s_camera}')")
        except :
            print("Already Exist")
       
    # Function to show camera frame while checking camera link is valid or not
    def show_frame(self):
        try:
            if validators.url(self.drop.focus()):
                if cam_on:
                    ret, frame = self.cap.read()
                    if ret:
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        img = Image.fromarray(cv2image).resize((480, 480))
                        imgtk = ImageTk.PhotoImage(image=img)
                        self.display1.imgtk = imgtk
                        self.display1.configure(image=imgtk)
                        self.display1.after(1, self.show_frame)
        except:
            print("wrong")
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
                        self.display1.after(1, self.show_frame)
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
                self.display1.after(1, self.show_frame)
        except:
            print("wrong")     
        # self.display1.configure(image=imgtk)
        # self.display1.after(1, self.show_frame)

    # Start video frames
    def start_vid(self):
        global cam_on
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        cam_on = True
        self.show_frame()

    # stop video frames
    def stop_vid(self):
        global cam_on
        cam_on = False
        if self.cap:
            self.cap.release()
            self.display1.config(image="")
            
    # function to open User Management 
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserPage(self.newWindow, path=os.path.join(os.getcwd(), 'FaceRecog', 'images'))

    def new_window_1(self):
        self.master.destroy()
        root = tk.Tk()
        Thread(target = lambda :[HomePageD(root),run()]).start()
        root.mainloop()

    # destroy window 
    def close_windows(self):
        self.master.destroy()
#==================================================================End==================================================
