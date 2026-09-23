
import os
import sqlite3

def seed_packages():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # New packages data
        new_packages = [
            # First batch (Custom Images / Unsplash fallback)
            ('Paris City Lights', '5 Days • 4 Nights', 4.8, 'Experience the romance of Paris with a Seine river cruise and Eiffel Tower dinner.', 1600, 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&h=400&fit=crop', 1),
            ('New York Skyline', '5 Days • 4 Nights', 4.7, 'Explore the city that never sleeps, from Times Square to Central Park.', 1900, 'https://images.unsplash.com/photo-1496442226666-8d4a0e62e6e9?w=600&h=400&fit=crop', 1),
            ('Rome Ancient Ruins', '6 Days • 5 Nights', 4.8, 'Walk through history in the Colosseum and Roman Forum.', 1700, 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=600&h=400&fit=crop', 1),
            ('Sydney Opera House', '7 Days • 6 Nights', 4.9, 'Discover the beauty of Sydney Harbour and the iconic Opera House.', 2100, 'https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=600&h=400&fit=crop', 1),
            
            # Second batch (Top Picks)
            ('Tokyo Neon Nights', '6 Days • 5 Nights', 4.8, 'Discover the vibrant culture and futuristic cityscape of Tokyo.', 2100, 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=600&h=400&fit=crop', 1),
            ('Swiss Alps Skiing', '7 Days • 6 Nights', 4.9, 'Ski through the breathtaking snow-capped mountains of Switzerland.', 2800, 'https://images.unsplash.com/photo-1551009175-8a68da93d5f9?w=600&h=400&fit=crop', 1),
            ('Amazon Rainforest Trek', '8 Days • 7 Nights', 4.7, 'Immerse yourself in the world\'s largest tropical rainforest.', 1900, 'https://images.unsplash.com/photo-1516934024742-b461fba47600?w=600&h=400&fit=crop', 1),
            ('Dubai Desert Safari', '5 Days • 4 Nights', 4.8, 'Experience luxury and adventure in the heart of the desert.', 2300, 'https://images.unsplash.com/photo-1512453979798-5ea904ac66de?w=600&h=400&fit=crop', 1)
        ]
        
        # Check if packages already exist to avoid duplicates
        existing_names = [row[0] for row in cursor.execute("SELECT name FROM packages").fetchall()]
        
        added_count = 0
        for pkg in new_packages:
            if pkg[0] not in existing_names:
                cursor.execute("INSERT INTO packages (name, duration, rating, description, price, image_url, is_bestseller) VALUES (?, ?, ?, ?, ?, ?, ?)", pkg)
                added_count += 1
                
        # Update existing bestsellers if needed
        cursor.execute("UPDATE packages SET is_bestseller=1 WHERE id IN (2, 3)")
        
        conn.commit()
        print(f"Successfully added {added_count} new packages.")
        
        # Verify
        count = cursor.execute("SELECT count(*) FROM packages WHERE is_bestseller=1").fetchone()[0]
        print(f"Total bestsellers now: {count}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    seed_packages()
