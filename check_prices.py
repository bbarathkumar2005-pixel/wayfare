
import os
import sqlite3

try:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    params = cursor.execute("SELECT name, price FROM packages").fetchall()
    for p in params:
        print(f"{p[0]}: {p[1]}")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
