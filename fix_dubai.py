
import os
import sqlite3

def fix_dubai_image():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check current URL
        current = cursor.execute("SELECT image_url FROM packages WHERE name='Dubai Desert Safari'").fetchone()
        print(f"Current Dubai URL: {current[0] if current else 'Not Found'}")
        
        # New robust URL for Dubai (Dubai Marina / Skyline)
        # Using a completely different image ID to bypass potential caching/availability issues
        new_url = 'https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=800'
        
        print(f"Updating to: {new_url}")
        cursor.execute("UPDATE packages SET image_url=? WHERE name='Dubai Desert Safari'", (new_url,))
        conn.commit()
        print("Dubai image updated successfully.")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_dubai_image()
