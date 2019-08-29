import sqlite3
import os

class SQlite3:
  def __init__(self, dbName:str):
    # Convert db name 
    if (dbName.find(".db") == -1):
      self.dbName = dbName + ".db"
    else:
      self.dbName = dbName
    # Check if file exist - if exist connect to that database file, if not show the error
    if (os.path.isfile(self.dbName)):
      self.conn = sqlite3.connect(self.dbName)
      self.cursor = self.conn.cursor()
    else:
      print("Database file isn't exist !")
  def command(self,command=""):
    self.cursor.execute(command)
    self.conn.commit()
  
  
  
db = SQlite3("fuck")
db.command("""CREATE TABLE user(
  ID INT PRIMARY KEY,
  USERNAME TEXT NOT NULL UNIQUE,
  PASSWORD TEXT NOT NULL
);""")
# db.command("PRAGMA table_info(user);")
input()