import mysql.connector

mydb = mysql.connector.connect(host="localhost",port = "3306", user="root", passwd="Yc9920530982", database="gias",
                                           auth_plugin='mysql_native_password')

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
