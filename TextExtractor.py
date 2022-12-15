from pickletools import long1
import mysql.connector as mysql
import sqlite3
import books
import annotation
import datetime

APPLE_EPOCH_START = int((datetime.datetime(2001, 1, 1)-datetime.datetime.utcfromtimestamp(0)).total_seconds()*1000)

def convertAppleTimeSeconds(appleTime):
    return int(int(APPLE_EPOCH_START + (appleTime * 1000))/1000);

def convertAppleTimeMilliSeconds(appleTime):
    return int(int(APPLE_EPOCH_START + (appleTime * 1000)));

cursor_db_connection = None;

def main():
  global cursor_db_connection

  # CONSTANTS
  TITLE = "ZTITLE"
  AUTHOR = "ZAUTHOR"
  BOOKID = "ZASSETID"

  COLOR = "ZANNOTATIONSTYLE"
  CONTENT = "ZANNOTATIONSELECTEDTEXT"
  PARAGRAPH = "ZFUTUREPROOFING5"
  NOTE = "ZANNOTATIONNOTE"
  CREATEDTIME = "ZANNOTATIONCREATIONDATE"
  MODIFIEDTIME = "ZANNOTATIONMODIFICATIONDATE"
  LOCATIONRANGESTART = "ZPLLOCATIONRANGESTART"

  BOOKSTABLE = "ZBKLIBRARYASSET"
  ANNOTATIONSTABLE = "ZAEANNOTATION"

  # VARIABLES
  array_books = []
  array_annotations = []
  i=0

  # TEXT ANNOTATION AND BOOKS DATABASES
  conn_Text = sqlite3.connect('Database/Annotations.sqlite')
  cursor_Text = conn_Text.cursor()
  conn_books = sqlite3.connect('Database/books.sqlite')
  cursor_books = conn_books.cursor()

  # Connect to MySQL server
  HOST = ""
  DATABASE = ""
  USER = ""
  PASSWORD = ""

  db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
  cursor_db_connection = db_connection.cursor()
  print("Connected to:", db_connection.get_server_info())

  # Get all books
  cursor_books.execute("select "+BOOKID+" as ID, "+TITLE+" as TITLE, "+AUTHOR+" as AUTHOR from "+BOOKSTABLE+" order by "+BOOKID)

  # Insert all books into an array
  recordsNotes = cursor_books.fetchall()

  for row in recordsNotes:
    array_books.append(books.book(row[0], row[1], row[2]))

    # Get all annotations of that book
    cursor_Text.execute("SELECT "+COLOR+", "+CREATEDTIME+", "+MODIFIEDTIME+", "+PARAGRAPH+", "+NOTE+", "+LOCATIONRANGESTART+", "+CONTENT+" FROM "+ANNOTATIONSTABLE+" WHERE ZANNOTATIONDELETED = 0 AND "+CONTENT+" != 'NULL' AND ZANNOTATIONASSETID = '" + row[0] + "' order by ZANNOTATIONASSETID, "+LOCATIONRANGESTART )

    # Insert all annotations into an array
    recordsNotes = cursor_Text.fetchall()

    for annotationRow in recordsNotes:
        #Check if Chapter field is NULL
        if(annotationRow[3]==None):
            array_annotations.append(annotation.annotation(row[0], row[1], row[2], annotationRow[0], convertAppleTimeSeconds(annotationRow[1]), convertAppleTimeSeconds(annotationRow[2]), "NULL", annotationRow[4], annotationRow[5], annotationRow[6].rstrip()))
        else:
            array_annotations.append(annotation.annotation(row[0], row[1], row[2], annotationRow[0], convertAppleTimeSeconds(annotationRow[1]), convertAppleTimeSeconds(annotationRow[2]), annotationRow[3].rstrip(), annotationRow[4], annotationRow[5], annotationRow[6].rstrip()))

  # Get all existing annotations from the database
  cursor_db_connection.execute("Select * from TEXTNOTES")
  recordsNotes = cursor_db_connection.fetchall()

  alreadyexist = False
  for recordsNotesText in array_annotations:
    # Check if the annotation already exist
    for row in recordsNotes:
      if(str(row[6]) == str(recordsNotesText.getContent()) and str(row[1]) == str(recordsNotesText.getCreatedTime())):
        alreadyexist = True
        print("Already exist")
        break
    # If the annotation doesn't exist, insert it in the database
    if(alreadyexist == False):
      # Check if the author already exist, if not insert it
      if(checkifAuthorExist(recordsNotesText.getAuthor()) == False):
          cursor_db_connection.execute("INSERT INTO AUTHORS (Name) VALUES ('"+recordsNotesText.getAuthor()+"')")
          db_connection.commit()
      authorID = getAuthorID(recordsNotesText.getAuthor())
      # Check if the book already exist, if not insert it
      if(checkifBookExist(recordsNotesText.getBookTitle()) == False):
          cursor_db_connection.execute("INSERT INTO BOOKS (Title, AuthorID) VALUES ('"+recordsNotesText.getBookTitle()+"', '"+str(authorID)+"')")
          db_connection.commit()
      bookID = getBookID(recordsNotesText.getBookTitle())
      # Insert the annotation
      cursor_db_connection.execute("INSERT INTO TEXTNOTES (CreatedTime, Style, Paragraph, PersonalNote, content, AuthorID, BookID) VALUES ("+str(recordsNotesText.getCreatedTime())+", "+recordsNotesText.getColor()+", '"+recordsNotesText.getParagraph().replace("'", "''" )+"', '"+recordsNotesText.getNote()+"', '"+recordsNotesText.getContent().replace("'", "''" )+"', '"+str(authorID)+"', '"+str(bookID)+"')")
      db_connection.commit()
      print("Inserted")
    alreadyexist = False

# Function to check if the author already exist in the database table
def checkifAuthorExist(author):
  cursor_db_connection.execute("SELECT * FROM AUTHORS WHERE Name = '"+author+"'")
  recordsNotes = cursor_db_connection.fetchall()
  if(len(recordsNotes) == 0):
    return False
  else:
    return True

# Function to check if the book already exist in the database table
def checkifBookExist(book):
  cursor_db_connection.execute("SELECT * FROM BOOKS WHERE Title = '"+book+"'")
  recordsNotes = cursor_db_connection.fetchall()
  if(len(recordsNotes) == 0):
    return False
  else:
    return True

# Function to get the author ID
def getAuthorID(author):
  cursor_db_connection.execute("SELECT ID FROM AUTHORS WHERE Name = '"+author+"'")
  recordsNotes = cursor_db_connection.fetchall()
  for row in recordsNotes:
    return row[0]

# Function to get the book ID
def getBookID(book):
  cursor_db_connection.execute("SELECT ID FROM BOOKS WHERE Title = '"+book+"'")
  recordsNotes = cursor_db_connection.fetchall()
  for row in recordsNotes:
    return row[0]

# Main function
if __name__ == "__main__":
  main();
  print("Process completed")