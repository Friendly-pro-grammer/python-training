import sqlite3
import os 
working_dir = os.path.dirname(os.path.abspath(__file__))
to_path = os.path.join(working_dir,"tutorials.db")
con = sqlite3.connect(to_path)
#cursor
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                department TEXT
                )
            """)
# cur.execute("""
#             INSERT INTO users(id,name,age,department)
#             VALUES (1,"amit",22,"CE"), (2,"John",21,"EC"), (3,"DOE",23,"Civil")
#             """)
con.commit()
cur.execute("SELECT * FROM users")
USERS = cur.fetchall()
for user in USERS:
    print(user)
con.close()
cur.execute("""
            UPDATE users
            
            """)