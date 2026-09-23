
import os
import sqlite3

try:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    params = cursor.execute("SELECT name, image_url FROM packages WHERE name IN ('New York Skyline', 'Dubai Desert Safari')").fetchall()
    print(params)
    conn.close()
except Exception as e:
    print(f"Error: {e}")
