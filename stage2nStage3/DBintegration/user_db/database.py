import sqlite3
import os
DATABASE_NAME = "app.db"
script_dir = os.path.dirname(os.path.abspath(__file__))
path_to  = os.path.join(script_dir,DATABASE_NAME)



def get_connection():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        
        connection.execute("PRAGMA foreign_keys=ON")
        return connection
    except sqlite3.Error as e:
        print(f"Database Connection Failed:{e}")
        raise
