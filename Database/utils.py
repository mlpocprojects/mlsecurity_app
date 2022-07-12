from tkinter.font import names
import mysql.connector
import os
from threading import Thread

# mydb = mysql.connector.connect(host="localhost",port = "3306", user="root", passwd="Yc9920530982", database="gias",
#                                            auth_plugin='mysql_native_password')
# database connection
mydb = mysql.connector.connect(host="43.231.124.114",port = "3306", user="parag", passwd="parag",
                                           auth_plugin='mysql_native_password')
user_db = "Gais.tb_user"
camera_db = "Gais.tb_camera"


def executor(db,query):
    mycursor = db.cursor()
    mycursor.execute(query)
    print("Successful run")
    mycursor.close()
    db.commit()

def get_list(db, query, c_values):
    mycursor = db.cursor()
    mycursor.execute(query)
    ans = mycursor.fetchall()
    for i in ans:
        c_values.append(i)

       
        
def entries(path = os.path.join(os.getcwd(), 'FaceRecog', 'images')):
    folders = os.listdir(path)
    # get_list(mydb,f"select image_name from {user_db} ", c_values = image_names)
    # print(len(image_names))
    for folder in folders:
        for name in os.listdir(os.path.join(path,folder)):
            try:
                executor(mydb,f"Insert into {user_db} values('{folder}','{os.path.join(path,folder)}','{name}')")
            except:
                print("Already exist")

def threadentries():
    t3 = Thread(target = entries(path = os.path.join(os.getcwd(), 'FaceRecog', 'images')))
    t3.start()

