#First of all check if you have installed folium library,
#if not "pip install folium geopy"

# import folium  # Import folium for creating maps
from geopy.geocoders import Nominatim  # Import Nominatim geocoder from geopy

# Initialize the geolocator with a user agent
geolocator = Nominatim(user_agent="my_geocoder_app")

# Get user input for an address
address = input("Enter an address to map: ")

# Try to get the geographical coordinates of the address
location = geolocator.geocode(address)

if location:
    lat, lon = location.latitude, location.longitude  # Fixed typo (latitude, not latidude)
else:
    print("Address not found! Defaulting to White House.")
    lat, lon = 38.8977, -77.0365  # Default coordinates for the White House

# Create a folium map centered at the obtained coordinates
m = folium.Map(location=[lat, lon], zoom_start=15)

# Add a marker to the map
folium.Marker(
    location=[lat, lon],
    popup=address if location else "White House",  # Display address or default location
    icon=folium.Icon(color="blue")  # Blue marker icon
).add_to(m)

# Save the map as an HTML file and inform the user
m.save("map.html")  
print("Map saved as map.html. Open it in your browser to view.")
