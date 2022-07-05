from Database.utils import mydb

mydb = mydb

def executor(db,query):
    mycursor = db.cursor()
    mycursor.execute(query)
    print("Successful run")
    mycursor.close()
    db.commit()

