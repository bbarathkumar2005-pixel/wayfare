
import os
import sqlite3

def check_schema():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("Destinations Schema:")
        schema = cursor.execute("PRAGMA table_info(destinations)").fetchall()
        for col in schema:
            print(col)
            
        print("\nPackages Schema:")
        schema = cursor.execute("PRAGMA table_info(packages)").fetchall()
        for col in schema:
            print(col)
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_schema()
