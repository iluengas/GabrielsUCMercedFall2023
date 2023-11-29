import sqlite3
import datetime

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(id, username, bio, profile_picture, creation_date, views):
    try:
        sqliteConnection = sqlite3.connect('instance/main.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_blob_query = """ INSERT INTO Users
                                  (id, username, bio, profile_picture, creation_date, views) VALUES (?, ?, ?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(profile_picture)
        # resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (id, username, bio, empPhoto, creation_date, views)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

currentDateTime = datetime.datetime.now()
insertBLOB(1, "Smith", "test bio", r"C:\Users\gabeb\Documents\Fall2023\Fall2023\CSE111\ProjectFolder\static\images\pokemon\Aron.png", currentDateTime, 0)
