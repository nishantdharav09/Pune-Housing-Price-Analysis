# Pune-Housing-Price-Analysis
An interactive geospatial visualization of property prices across Pune using Python, Folium, and CSV data.


🏠 Pune House Price Map

An interactive Pune House Price Map built with Python and Folium. The project displays different locations in and around Pune on an interactive map, with the house/property price shown when a marker is clicked.

📌 Project Overview

This project visualizes property prices at multiple Pune locations using an interactive map.

The Python program creates a Folium map centered on Pune and adds location markers with their corresponding prices. The generated map is saved as clean_map.html.

The project currently contains 5 rows in the CSV dataset and maps multiple Pune-area locations.

✨ Features

🗺️ Interactive Pune map

📍 Location markers

💰 Property price displayed in marker popups

🌐 OpenStreetMap-based map

🐍 Built using Python and Folium

📄 CSV dataset for house/property information

💾 Generates a standalone clean_map.html file

🛠️ Technologies Used

Python

Folium

Pandas

HTML

CSV

OpenStreetMap

📂 Project Structure

Pune-House-Price-Map/
│
├── project.py        # Python program that creates the map
├── house.csv         # House/property dataset
├── clean_map.html    # Generated interactive map
└── README.md         # Project documentation

▶️ How to Run

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-LINK>
cd Pune-House-Price-Map

2. Install required libraries

pip install folium pandas

3. Run the Python program

python project.py

After running the program, clean_map.html will be generated.

4. Open the map

Open clean_map.html in a web browser to view the interactive map.

📍 Example Locations

The project includes locations such as:

Kothrud

Hinjewadi

Baner

Wakad

Aundh

Wagholi

Bakhori Phata

Hadapsar

Kharadi

Viman Nagar

Shivaji Nagar

Koregaon Park

Pimpri-Chinchwad

Talegaon

Chakan

Magarpatta

Kalyani Nagar

Yerwada

Lohegaon

Dhanori

Undri

NIBM Road

Sinhagad Road

Warje

Karve Nagar

Bavdhan

Pashan

Sus

Balewadi

Ravet

Akurdi

Nigdi

🧠 How It Works

The Python program creates a Folium map centered on Pune:

m = folium.Map(location=[18.5204, 73.8567], zoom_start=11)

It then stores location, latitude, longitude, and price information and adds each location as a marker. When a marker is clicked, the location name and price are displayed in a popup.

The generated map uses OpenStreetMap tiles.

📊 Sample Data

Example property-price entries used by the project include:

Location

Price

Kothrud

₹5,00,000

Hinjewadi

₹10,00,000

Baner

₹15,00,000

Wakad

₹20,00,000

Aundh

₹25,00,000

Wagholi

₹12,00,000

Bakhori Phata

₹9,00,000

🎯 Project Objective

The main objective is to demonstrate how Python can be used to create an interactive geographical visualization of property prices.

🚀 Future Improvements

Add a price filter

Add search by location

Read all map data directly from the CSV file

Add different marker colors based on price range

Add charts for price comparison

Add a machine-learning model for house-price prediction

Deploy the interactive map online

👨‍💻 Author

Nishant Dharav

GitHub: https://github.com/nishantdharav09

⭐ If you find this project useful, consider giving the repository a star!
