# Imports 
import shutil
from tkinter import *
import tkinter as tk
import os
import re
from tkinter import ttk, filedialog
# SkyBlue3SteelBlue4
#242C35
#grey50

#===============================================================UserPage==============================================
class UserPage:
    def __init__(self, master,path):
        global username,my_entry
        username = tk.StringVar()
        self.nodes = dict()
        self.master = master
        self.master.title('User-Management')
        self.master.geometry("900x900")
        self.master.configure(bg='grey50')
        self.master.state('zoomed')
        
        # all Child frames inside main frame 
        self.frame4 = tk.Frame(self.master,bg='grey50')
        self.frame5 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50')
        self.frame6 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50')
        self.frame7 = tk.Frame(self.frame4, highlightbackground="#242C35", highlightthickness=3, bg='grey50')

        # Heading for frame 
        self.lab1 = tk.Label(self.frame6, text ="USER MANAGEMENT", bg = 'grey50',width=15,font=("Helvetica",16,'bold'), fg='white')
        # Search entry
        self.my_entry = tk.Entry(self.frame6,font=("Helvetica",20,'bold'))
        # search button
        self.searchbutton = tk.Button(self.frame6,text="SEARCH",font=("Helvetica",14,'bold'),command=self.search, width=15,bg="#242C35", fg='white')

        # alignment for above 
        self.lab1.pack(expand = True,padx=300,pady=0, fill= 'x',side = TOP)
        self.searchbutton.pack(expand = True,padx=300,pady=10, fill= 'x',side = BOTTOM)
        self.my_entry.pack(expand = True,padx=150, fill= 'x',side = BOTTOM)

        # adding tree view to frame
        self.ysb = Scrollbar(self.frame6, orient='vertical')
        self.xsb = Scrollbar(self.frame6, orient='horizontal')  
        s = ttk.Style()
        s.configure('Treeview.Heading',  font=("Helvetica",12,'bold'))

        self.tree = ttk.Treeview(self.frame6, height= 30,yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.tree.heading('#0', text='EXISTING USERS', anchor='w')
        self.tree.column("#0",anchor=CENTER, stretch=NO, width=500)
        self.ysb.config(command=self.tree.yview)
        self.ysb.config(command=self.tree.xview)
        #alignment for treeview
        self.tree.pack(side = LEFT, expand = True, padx=5, pady=20)

        # button for user Management 
        self.AddUser = tk.Button(self.frame7,text='ADD USER',font=("Helvetica",12,'bold'),command=self.press,height=3, width=20 , bg ="#242C35", fg='white' )
        self.UploadButton = tk.Button(self.frame7, text='UPDATE USER',font=("Helvetica",12,'bold'),command= lambda : [self.selection_but(),self.master_destory()],height=3, width=20 , bg ="#242C35", fg='white')
        self.DeleteButton = tk.Button(self.frame7, text='DELETE USER / IMAGE',font=("Helvetica",12,'bold'),command= lambda:[self.delete()],height=3, width=20 , bg ="#242C35", fg='white')
        self.BrowserButton = tk.Button(self.frame7, text='BROWSE USER',font=("Helvetica",12,'bold'),command= lambda: [self.Brower_but()],height=3, width=20 , bg ="#242C35", fg='white')

        # alignment 
        self.DeleteButton.pack(padx=150, pady=42,fill= 'both', side = BOTTOM)
        self.BrowserButton.pack(padx=150, pady=42,fill= 'both', side = BOTTOM)
        self.UploadButton.pack(padx=150, pady=42,fill= 'both', side = BOTTOM)
        self.AddUser.pack(padx=150, pady=42,fill= 'both', side = BOTTOM)

        # frame alignment 
        self.frame4.pack(fill="both", expand=True)
        self.frame6.pack(side = LEFT, expand=True, anchor= NW,padx=30, pady=30, fill=BOTH)
        self.frame7.pack(side = LEFT, expand=True, anchor =N,padx=30, pady=30, fill=BOTH)

        # inserting folder and images into treeview structure
        self.ids = []
        self.folders = os.listdir(path)
        for folder in self.folders:
            self.ids.append(self.tree.insert('', 'end', folder, text=folder))
            for name in os.listdir(os.path.join(path,folder)):
                self.tree.insert(folder, 'end', name, text=name)

    # Delete Functionality
    def delete(self):
        # Get selected item to Delete
        selected_item = self.tree.focus()
        # selected_item_1 = selected_item.split('.')[0]
        try:
            if selected_item.split('.')[1].lower() == 'jpg':
                temp = re.compile("([a-zA-Z]+)([0-9]+)")
                selected_item_1 = temp.match(selected_item).groups()[0]
                os.remove(str(os.path.join(os.getcwd(),'Face_Recog','images',selected_item_1, str(selected_item))))
        except :
                print("wrong")
        try:
                temp = re.compile("([a-zA-Z]+)([0-9]+)")
                selected_item_1 = selected_item.split('.')[0]
                os.remove(str(os.path.join(os.getcwd(),'Face_Recog','images',selected_item_1, str(selected_item))))
        except :
            print("wrong")
            shutil.rmtree(os.path.join(os.getcwd(),'Face_Recog','images',str(selected_item)))
        finally:
            self.tree.delete(selected_item)

    # Browse Image/folder functionality
    def Brower_but(self):
        name = str(self.tree.focus())
        if len(name) == 0:
            print("Please add a username")
        else:
            pass
        self.filename = filedialog.askopenfilenames(parent =self.frame5,initialdir=str(os.path.join(os.getcwd(),'Face_Recog','images', str(name))),filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    # Upload functionality Button
    def selection_but(self):
        global root
        self.root = tk.Tk()
        name = str(self.tree.focus())
        self.file = filedialog.askopenfilenames(parent =self.frame5,initialdir=str(os.path.join(os.getcwd(),'Face_Recog','images', str(name))),filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if len(name) == 0:
            print("Please add a username")
        else:
            pass
        if not os.path.isdir(str(os.getcwd()) + "\Face_Recog"):
            os.mkdir(str(os.getcwd()) + "\Face_Recog")
            os.mkdir(str(os.getcwd()) + "\Face_Recog\images")
        else:
            pass
        for i in self.root.splitlist(self.file):
            print(i)
            shutil.copy(i, str(os.getcwd() + r"/Face_Recog/images/" + str(name)))
            print(str(os.getcwd() + r"\Face_Recog\images"))
            print("Complete transfer")
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

    # Update image in folder 
    def press(self):
        global user
        user = tk.StringVar()
        self.lab1 = tk.Label(self.frame7, text="Username",bg ="grey50",font=("Helvetica",16,'bold'), fg='white')
        user = tk.Entry(self.frame7, textvariable=user,font=("Helvetica",14,'bold'))
        self.addButton = tk.Button(self.frame7, text='Browse',font=("Helvetica",14,'bold'),command=lambda :[self.Upload_New(), self.master_destory()],bg ="#242C35", fg='white')

        self.lab1.pack(side = TOP, pady= 3)
        user.pack(side = TOP, pady= 3)
        self.addButton.pack(side = TOP, pady= 3)

    # Update image in folder called by press function
    def Upload_New(self):
        global root
        self.root = tk.Tk()
        file = filedialog.askopenfilenames(parent=self.frame5, title='Choose a File',filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        name = user.get()
        if len(name) == 0:
            print("Please add a username")
        else:
            pass
        if not os.path.isdir(str(os.getcwd()) + "\Face_Recog"):
            os.mkdir(str(os.getcwd()) + "\Face_Recog")
            os.mkdir(str(os.getcwd()) + "\Face_Recog\images")
        else:
            pass
        if not os.path.isdir(str(os.getcwd()) + "\Face_Recog\images/" + str(name)):
            os.mkdir(str(os.getcwd()) + "\Face_Recog\images/" + str(name))
            for i in self.root.splitlist(file):
                print(i)
                shutil.copy(i, str(os.getcwd() + r"/Face_Recog/images/" + str(name)))
                print(str(os.getcwd() + r"\Face_Recog\images"))
                print("Complete transfer")
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
        self.app = UserPage(self.newWindow, path=os.path.join(os.getcwd(), 'Face_Recog', 'images'))
#=====================================================================End==========================================================