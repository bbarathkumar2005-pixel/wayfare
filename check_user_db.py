
import os
import sqlite3
from werkzeug.security import check_password_hash

def check_user():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    email = "newuser@example.com"
    user = cur.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    
    if user:
        print(f"User found: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Hash: {user['password_hash']}")
        
        # Test password
        password = "password123"
        is_valid = check_password_hash(user["password_hash"], password)
        print(f"Password '{password}' is valid: {is_valid}")
    else:
        print("User NOT found in database")
        
    conn.close()

if __name__ == "__main__":
    check_user()
