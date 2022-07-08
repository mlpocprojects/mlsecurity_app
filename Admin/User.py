# Imports 
import shutil
from tkinter import *
import tkinter as tk
import os
import re
from tkinter import ttk, filedialog
from turtle import left
# SkyBlue3SteelBlue4
#242C35
#grey50
from Database.utils import *


#===============================================================UserPage==============================================
class UserPage:
    def __init__(self, master,path):
        global username,my_entry
        username = tk.StringVar()
        self.nodes = dict()
        self.master = master
        self.master.title('User-Management')
        self.master.geometry("1000x650")
        self.master.configure(bg='grey50')
        self.master.resizable(0,0)

        # self.master.state('zoomed')
        
        # all Child frames inside main frame 
        self.frame4 = tk.Frame(self.master,bg='grey50')
        self.frame5 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50')
        self.frame6 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50', width= 100)
        self.frame7 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50')

        # Search entry
        self.my_entry = tk.Entry(self.frame6,font=("Helvetica",20,'bold'), width = 30)
        # search button
        self.searchbutton = tk.Button(self.frame6,text="SEARCH",font=("Helvetica",14,'bold'),command=self.search, width=30,bg="#242C35", fg='white')

        # alignment for above 
        self.searchbutton.pack(padx = 55 ,pady=5,side = BOTTOM)
        self.my_entry.pack(side = BOTTOM)

        # adding tree view to frame
        self.ysb = Scrollbar(self.frame6, orient='vertical')
        self.xsb = Scrollbar(self.frame6, orient='horizontal')  
        s = ttk.Style()
        s.configure('Treeview.Heading',  font=("Helvetica",12,'bold'))

        self.tree = ttk.Treeview(self.frame6, height= 30,yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.tree.heading('#0', text='EXISTING USERS', anchor='w')
        self.tree.column("#0",anchor=CENTER, stretch=NO, width=400)
        self.ysb.config(command=self.tree.yview)
        self.ysb.config(command=self.tree.xview)
        #alignment for treeview
        self.tree.pack(side = BOTTOM, pady=20)

        # button for user Management 
        self.AddUser = tk.Button(self.frame7,text='ADD USER',font=("Helvetica",12,'bold'),command=self.press,height=3, width=20 , bg ="#242C35", fg='white' )
        self.UpdateButton = tk.Button(self.frame7, text='UPDATE USER',font=("Helvetica",12,'bold'),command= lambda : [self.update_Bu(),self.master_destory()],height=3, width=20 , bg ="#242C35", fg='white')
        self.DeleteButton = tk.Button(self.frame7, text='DELETE USER / IMAGE',font=("Helvetica",12,'bold'),command= lambda:[self.delete(),self.master_destory()],height=3, width=20 , bg ="#242C35", fg='white')
        self.BrowserButton = tk.Button(self.frame7, text='BROWSE USER',font=("Helvetica",12,'bold'),command= lambda: [self.Brower_but()],height=3, width=20 , bg ="#242C35", fg='white')

        # alignment 
        self.DeleteButton.pack(padx=150, pady=30,fill= 'both', side = BOTTOM)
        self.BrowserButton.pack(padx=150, pady=30,fill= 'both', side = BOTTOM)
        self.UpdateButton.pack(padx=150, pady=30,fill= 'both', side = BOTTOM)
        self.AddUser.pack(padx=150, pady=30,fill= 'both', side = BOTTOM)

        # frame alignment 
        self.frame4.pack()
        self.frame7.pack(side = LEFT, fill=BOTH)
        self.frame6.pack(side = LEFT, fill=BOTH)

        # inserting folder and images into treeview structure
        self.ids = []
        self.folders = os.listdir(path)
        for folder in self.folders:
            self.ids.append(self.tree.insert('', 'end', folder, text=folder))
            for name in os.listdir(os.path.join(path,folder)):
                self.tree.insert(folder, 'end', name, text=name)
                # try:
                #     executor(mydb,f"Insert into gias.db_user values('{folder}','{os.path.join(path,folder)}','{name}')")
                # except:
                #     print("Already exist")

    # Delete Functionality
    def delete(self):
        # Get selected item to Delete
        selected_item = self.tree.focus()
        try:
            for file in os.listdir(os.path.join(os.getcwd() ,"FaceRecog","images")):
                for i in os.listdir(os.path.join(os.getcwd() ,"FaceRecog","images",file)):
                    try:
                        os.remove(os.path.join(os.getcwd() ,"FaceRecog","images",file,selected_item))
                        # executor(mydb,f"DELETE FROM gias.db_user WHERE image_name='{selected_item}'")
                    except:
                        print("no")
                # write for delete with number image
                #DELETE FROM gias.db_user WHERE image_name='cc.jpg';
        except :
                print("wrong")
        try:
            shutil.rmtree(os.path.join(os.getcwd(),'FaceRecog','images',str(selected_item)))
            # executor(mydb,f"DELETE FROM gias.db_user WHERE user_name='{selected_item}'")
        except:
            print("wrong")
        finally:
            self.tree.delete(selected_item)

    # Browse Image/folder functionality
    def Brower_but(self):
        name = str(self.tree.focus())
        if len(name) == 0:
            print("Please add a username")
        else:
            pass
        self.filename = filedialog.askopenfilenames(parent =self.frame5,initialdir=str(os.path.join(os.getcwd(),'FaceRecog','images', str(name))),filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    # Upload new image to existing user Button
    def update_Bu(self):
        global root
        self.root = tk.Tk()
        name = str(self.tree.focus())
        self.file = filedialog.askopenfilenames(parent =self.frame5,initialdir=str(os.path.join(os.getcwd(),'FaceRecog','images', str(name))),filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if len(name) == 0:
            print("Please Select User")
        else:
            pass
        for i in self.root.splitlist(self.file):
            print(i)
            shutil.copy(i, str(os.getcwd() + r"/FaceRecog/images/" + str(name)))
            print(str(os.getcwd() + r"\FaceRecog\images"))
            print("Complete transfer")
            path = os.getcwd() + r"/FaceRecog/images/" + str(name) + "/" + i.split('/')[-1]
            # executor(mydb,f"INSERT INTO gias.db_user values('{str(name)}','{path}','{i.split('/')[-1]}')")
        self.root.destroy()

    '''
    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))
    '''

    # Search in treeview for user
    def search(self):
        self.my_entry.get()
        self.selections = []
        for i in range(len(self.folders)):
            if self.my_entry.get() != "" and self.my_entry.get().lower() == self.folders[i][:len(self.my_entry.get())].lower():
                self.selections.append(self.ids[i]) #if it matches it appends the id to the selections list
        self.tree.selection_set(self.selections) #we then select every id in the list

    # Add new user 
    def press(self):
        global user
        user = tk.StringVar()
        self.lab1 = tk.Label(self.frame7, text="Username",bg ="grey50",font=("Helvetica",16,'bold'), fg='white')
        user = tk.Entry(self.frame7, textvariable=user,font=("Helvetica",14,'bold'))
        self.addButton = tk.Button(self.frame7, text='Browse',font=("Helvetica",14,'bold'),command=lambda :[self.Upload_New(), self.master_destory()],bg ="#242C35", fg='white')

        self.lab1.pack(side = TOP, pady= 3)
        user.pack(side = TOP, pady= 3)
        self.addButton.pack(side = TOP, pady= 3)

    # Add new user image connected with press function
    def Upload_New(self):
        global root
        self.root = tk.Tk()
        file = filedialog.askopenfilenames(parent=self.frame5, title='Choose a File',filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        name = user.get()
        if len(name) == 0:
            print("Please add a username")
        else:
            pass
        if not os.path.isdir(str(os.getcwd()) + "\FaceRecog"):
            os.mkdir(str(os.getcwd()) + "\FaceRecog")
            os.mkdir(str(os.getcwd()) + "\FaceRecog\images")
        else:
            pass
        if not os.path.isdir(str(os.getcwd()) + "\FaceRecog\images/" + str(name)):
            os.mkdir(str(os.getcwd()) + "\FaceRecog\images/" + str(name))
            for i in self.root.splitlist(file):
                print(i)
                shutil.copy(i, str(os.getcwd() + r"/FaceRecog/images/" + str(name)))
                print(str(os.getcwd() + r"\FaceRecog\images"))
                print("Complete transfer")
                # dbase = mydb
                # path = os.getcwd() + r"/FaceRecog/images/" + str(name) + "/" + i.split('/')[-1]
                # executor(dbase,f"INSERT INTO gias.db_user values('{str(name)}','{path}','{i.split('/')[-1]}')")
        else:
            print("This username already exists")
        self.root.destroy()

    # destroying window 
    def close_windows(self):
        self.master.destroy()
    
    # refresh
    def master_destory(self):
        self.master.destroy()
        self.new_window()

    # Refresh userpage when having update 
    def new_window(self):
        self.newWindow = tk.Toplevel()
        self.app = UserPage(self.newWindow, path=os.path.join(os.getcwd(), 'FaceRecog', 'images'))
#=====================================================================End==========================================================