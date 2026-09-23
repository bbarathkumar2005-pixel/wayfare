
import os
import sqlite3

def fix_images():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # New robust URLs
        new_urls = {
            'New York Skyline': 'https://images.unsplash.com/photo-1534430480872-3498386e7856?auto=format&fit=crop&w=800',
            'Dubai Desert Safari': 'https://images.unsplash.com/photo-1547234935-80c7142ee969?auto=format&fit=crop&w=800'
        }
        
        for name, url in new_urls.items():
            print(f"Updating {name}...")
            cursor.execute("UPDATE packages SET image_url=? WHERE name=?", (url, name))
            
        conn.commit()
        print("Images updated successfully.")
        
        # Verify
        params = cursor.execute("SELECT name, image_url FROM packages WHERE name IN ('New York Skyline', 'Dubai Desert Safari')").fetchall()
        print("New URLs:", params)
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_images()
