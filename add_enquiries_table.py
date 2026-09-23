import os
import sqlite3

def add_enquiries_table():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS enquiries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            email TEXT,
            subject TEXT,
            message TEXT,
            response TEXT,
            status TEXT DEFAULT 'Pending',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        print("Enquiries table created successfully.")
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    add_enquiries_table()
