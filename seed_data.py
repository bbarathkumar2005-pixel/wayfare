import os
import sqlite3
from werkzeug.security import generate_password_hash

def seed_data():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Seed Admin User
    admin_pass = generate_password_hash("admin123")
    try:
        cur.execute("INSERT INTO users(name, email, password_hash, role) VALUES (?, ?, ?, ?)",
                    ("Admin User", "admin@wayfare.com", admin_pass, "admin"))
        print("Admin user created.")
    except sqlite3.IntegrityError:
        print("Admin user already exists.")

    # Seed Destinations
    destinations = [
        ("Paris", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&h=600&fit=crop", 24),
        ("Maldives", "https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=800&h=600&fit=crop", 18),
        ("New York", "https://images.unsplash.com/photo-1529963183134-61a90db47eaf?w=800&h=600&fit=crop", 31),
        ("Dubai", "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=800&h=600&fit=crop", 27),
        ("Rome", "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800&h=600&fit=crop", 22),
        ("Stockholm", "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800&h=600&fit=crop", 15),
        ("Cape Town", "https://images.unsplash.com/photo-1528164344705-47542687000d?w=800&h=600&fit=crop", 19),
        ("Barcelona", "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800&h=600&fit=crop", 26),
    ]

    for dest in destinations:
        cur.execute("INSERT INTO destinations(name, image_url, tour_count) VALUES (?, ?, ?)", dest)
    
    print(f"Seeded {len(destinations)} destinations.")

    # Seed Packages
    packages = [
        ("Bali Island Escape", "7 Days • 6 Nights", 4.9, 
         "Experience the magic of Bali with temple visits, rice terraces, beach relaxation, and traditional ceremonies", 
         108000, "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600&h=400&fit=crop", 1, 0),
        
        ("Swiss Alps Adventure", "10 Days • 9 Nights", 5.0, 
         "Journey through stunning mountain landscapes, charming villages, scenic train rides, and world-class skiing", 
         208000, "https://images.unsplash.com/photo-1551632811-561732d1e306?w=600&h=400&fit=crop", 0, 1),
        
        ("Greek Island Hopping", "5 Days • 4 Nights", 4.8, 
         "Discover Santorini and Mykonos with stunning sunsets, white-washed architecture, and Mediterranean cuisine", 
         133000, "https://images.unsplash.com/photo-1513326738677-b964603b136d?w=600&h=400&fit=crop", 0, 0),
        
        ("Tokyo Cultural Journey", "8 Days • 7 Nights", 4.9, 
         "Immerse yourself in Japanese culture with temple visits, sushi-making classes, and modern city exploration", 
         158000, "https://images.unsplash.com/photo-1504893524553-b855bce32c67?w=600&h=400&fit=crop", 0, 0),
         
        ("Machu Picchu Explorer", "9 Days • 8 Nights", 5.0, 
         "Trek the Inca Trail to ancient ruins, explore Cusco's colonial charm, and experience Sacred Valley wonders", 
         150000, "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=600&h=400&fit=crop", 1, 0),
         
        ("Iceland Northern Lights", "6 Days • 5 Nights", 4.8, 
         "Witness Aurora Borealis, explore ice caves, relax in geothermal hot springs, and chase waterfalls", 
         183000, "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&h=400&fit=crop", 0, 0)
    ]

    for pkg in packages:
        cur.execute("""INSERT INTO packages(name, duration, rating, description, price, image_url, is_bestseller, is_premium) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", pkg)

    print(f"Seeded {len(packages)} packages.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()
