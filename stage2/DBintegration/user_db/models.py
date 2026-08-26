from database import get_connection
def create_table():
    connection =get_connection()
    try:
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           email TEXT NOT NULL
                       )
                       """)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Failed to create table:{e}")
        raise
    finally:
        connection.close()