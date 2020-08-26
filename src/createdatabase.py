import mysql.connector
import sys


# def insertImage():
#     try:
#         filePath = sys.argv[0]
#     except NotImplementedError:
#         print('Pass an image please as a parameter')


def insertImage(MyCursor, imagePath):
    with open(imagePath, 'rb') as File:
        BinaryData = File.read()
    SQLStatement = "INSERT INTO Images (Photo) VALUES (%s)"
    MyCursor.execute(SQLStatement, (BinaryData, ))


def retrieveId(MyCursor, id):
    SQLStatement = f"SELECT * FROM Images WHERE id = {str(id)}"
    MyCursor.execute(SQLStatement)
    MyResult = MyCursor.fetchone()[1]
    StoreFilePath = f"ImageOutputs/img{str(id)}.jpg"
    with open(StoreFilePath, 'wb') as File:
        File.write(MyResult)
        File.close()



def connectDatabase():
    MyDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="5321",
        database="Vacancii"
    )

    MyCursor = MyDB.cursor()

    MyCursor.execute("CREATE TABLE IF NOT EXISTS Images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")
    
    menu_input = input('1. Insert image\n 2. Read image')
    if int(menu_input) == 1:
        filePath = input("Enter file path")
        insertImage(MyCursor, filePath)
        MyDB.commit()
    elif int(menu_input) == 2:
        reqId = input("Enter ID: ")
        retrieveId(MyCursor, reqId)


connectDatabase()