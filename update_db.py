
import os
import sqlite3

def update_db():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # 1. Add description column to destinations if it doesn't exist
        try:
            cursor.execute("ALTER TABLE destinations ADD COLUMN description TEXT")
            print("Added description column to destinations.")
        except sqlite3.OperationalError:
            print("Description column already exists.")

        # 2. Seed Descriptions
        descriptions = {
            "Santorini": "Experience the magic of whitewashed buildings, blue-domed churches, and stunning sunsets over the Aegean Sea.",
            "Paris": "The City of Light awaits with its iconic landmarks, world-class art, and romantic atmosphere.",
            "New York": "Explore the city that never sleeps, from the bright lights of Times Square to the serenity of Central Park.",
            "Bali": "Discover a tropical paradise with lush rice terraces, ancient temples, and beautiful beaches.",
            "Rome": "Step back in time and explore the eternal city, home to the Colosseum and Vatican City.",
            "Sydney": "Enjoy the vibrant harbor, iconic Opera House, and beautiful beaches of Australia's largest city.",
            "Kyoto": "Immerse yourself in traditional Japan with stunning temples, gardens, and geisha districts.",
            "Swiss Alps": "Experience breathtaking mountain scenery, world-class skiing, and charming alpine villages.",
            "Costa Rica": "A haven for nature lovers, featuring rainforests, volcanoes, and incredible wildlife.",
            "Egypt": "Uncover the mysteries of the pharaohs with visits to the Pyramids of Giza and the Sphinx.",
            "Iceland": "Witness the land of fire and ice, with waterfalls, geysers, and the Northern Lights.",
            "Thailand": "Enjoy vibrant street life, ornate shrines, and beautiful tropical islands.",
            "Dubai": "Marvel at futuristic architecture, luxury shopping, and desert adventures."
        }
        
        for dest, desc in descriptions.items():
            # partial match for destination name
            cursor.execute("UPDATE destinations SET description = ? WHERE name LIKE ?", (desc, f"%{dest}%"))
            
        print("Seeded destination descriptions.")

        # 3. Update Prices to Lakhs
        # Rule: If price < 10000, multiply by 100 to make it Lakhs-ready (approx) or just set fixed values.
        # Actually, let's just update all known packages to specific high values to be safe.
        
        price_updates = {
            "Bali Island Escape": 150000,
            "Swiss Alps Adventure": 250000,
            "Greek Island Hopping": 180000,
            "Tokyo Cultural Journey": 210000,
            "Machu Picchu Explorer": 195000,
            "Iceland Northern Lights": 220000,
            "Paris City Lights": 160000,
            "New York Skyline": 190000,
            "Rome Ancient Ruins": 170000,
            "Sydney Opera House": 210000,
            "Tokyo Neon Nights": 215000,
            "Swiss Alps Skiing": 280000,
            "Amazon Rainforest Trek": 185000,
            "Dubai Desert Safari": 230000
        }
        
        for name, price in price_updates.items():
             cursor.execute("UPDATE packages SET price = ? WHERE name = ?", (price, name))
             
        print("Updated package prices to Lakhs format.")
        
        conn.commit()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    update_db()
