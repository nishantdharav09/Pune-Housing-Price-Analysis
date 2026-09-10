import folium

m = folium.Map(location=[18.5204, 73.8567], zoom_start=11)

# Add locations with price
locations = [
    ("Kothrud", 18.5074, 73.8077, 500000),
    ("Hinjewadi", 18.5910, 73.7389, 1000000),   
    ("Baner", 18.5590, 73.7868, 1500000),
    ("Wakad", 18.5975, 73.7898, 2000000),
    ("Aundh", 18.5610, 73.8070, 2500000),
    ("Wagholi", 18.5800, 73.9800, 1200000),
    ("Bakhori Phata", 18.6500, 74.0500, 900000),

    ("Hadapsar", 18.5089, 73.9260, 1800000),
    ("Kharadi", 18.5516, 73.9436, 2200000),
    ("Viman Nagar", 18.5679, 73.9143, 2400000),
    ("Shivaji Nagar", 18.5308, 73.8475, 2600000),
    ("Koregaon Park", 18.5362, 73.8950, 3000000),
    ("Pimpri-Chinchwad", 18.6298, 73.7997, 1700000),
    ("Talegaon", 18.7350, 73.6750, 1100000),
    ("Chakan", 18.7600, 73.8600, 1300000),

    # 🔥 Extra locations
("Magarpatta", 18.5167, 73.9317, 2300000),
("Kalyani Nagar", 18.5485, 73.9036, 2800000),
("Yerwada", 18.5520, 73.8787, 1900000),
("Lohegaon", 18.5814, 73.9239, 1600000),
("Dhanori", 18.5743, 73.9035, 1500000),
("Undri", 18.4529, 73.9000, 1400000),
("NIBM Road", 18.4765, 73.8997, 2100000),
("Sinhagad Road", 18.4575, 73.8077, 1700000),
("Warje", 18.4875, 73.8077, 1800000),
("Karve Nagar", 18.4890, 73.8167, 1750000),
("Bavdhan", 18.5136, 73.7730, 2200000),
("Pashan", 18.5416, 73.7925, 2100000),
("Sus", 18.5550, 73.7400, 2000000),
("Balewadi", 18.5700, 73.7800, 2400000),
("Ravet", 18.6510, 73.7450, 1600000),
("Akurdi", 18.6500, 73.7700, 1500000),
("Nigdi", 18.6570, 73.7700, 1550000)
]

for name, lat, lon, price in locations:
    folium.Marker(
        location=[lat, lon],
        popup=f"{name}<br>Price: ₹{price}"
        # ❌ tooltip removed
    ).add_to(m)

m.save("clean_map.html")
print("Clean map ready!")