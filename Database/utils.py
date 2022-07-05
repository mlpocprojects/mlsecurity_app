import mysql.connector

mydb = mysql.connector.connect(host="localhost",port = "3306", user="root", passwd="Yc9920530982", database="gias",
                                           auth_plugin='mysql_native_password')