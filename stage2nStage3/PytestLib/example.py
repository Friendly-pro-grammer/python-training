import sqlite3
import pytest
@pytest.fixture
def db():
    connection = sqlite3.connect(":memory:")
    connection.execute("""
                       CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
                       """)
    yield connection
    connection.close()
def test_inser_user_db(db):
    db.execute("INSERT INTO users (name) VALUES (?)",("Alice",))
    cursor = db.execute("SELECT name FROM users")
    row  = cursor.fetchone()
    assert row[0]=="Alice"