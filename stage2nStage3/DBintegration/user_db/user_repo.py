from database import get_connection
def create_user(name,email):
    connection = get_connection()
    try:
        cursor  = connection.cursor()
        cursor.execute("""
                       INSERT INTO users (name,email)
                       VALUES(?,?)
                       """,(name,email)
                       )
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        print(f"failed to add user:{e}")
        raise
    finally:
        connection.close()
def get_all_users():
    connection = get_connection()
    try:
        cur = connection.cursor()
        cur.execute("""
                    SELECT * FROM users ORDER BY id
                    """)
        return cur.fetchall()
    except Exception as e:
        print(f"failed to fetch users:{e}")
        raise
    finally:
        connection.close()
def get_user_by_id(user_id):
    connection  = get_connection()
    try:
        cur = connection.cursor()
        cur.execute("""
                    SELECT * FROM users WHERE id=?
                    """,(user_id,))
        return cur.fetchone()
    except Exception as e:
        print(f"Failed to get user by id:{e}")
        raise
    finally:
        connection.close()
def update_user(id,name,email):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
                      UPDATE users
                      SET name = ?, email = ?
                      WHERE id = ? 
                       """,(name,email,id))
        connection.commit()
        return cursor.rowcount
    except Exception as e:
        connection.rollback()
        print(f"failed to update user{e}")
        raise
    finally:
        connection.close()
def delete_user(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        connection.commit()
        return cursor.rowcount

    except Exception as e:
        connection.rollback()
        print(f"Failed to delete user: {e}")
        raise

    finally:
        connection.close()
