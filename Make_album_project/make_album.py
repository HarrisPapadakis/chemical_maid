def make_album(artist, title, num_songs=None):  
    """Creates and returns a dictionary for a music album"""  
    album = {"artist": artist, "title": title}  # Create a dictionary with artist and title  
    if num_songs:  # If num_songs is provided, add it to the dictionary  
        album["num_songs"] = num_songs  
    return album  # Return the album dictionary  

# Create three albums  
album1 = make_album("Linkin Park", "Meteora")  
album2 = make_album("Linkin Park", "Hybrid Theory", 16)  
album3 = make_album("Linkin Park", "From Zero", 11)  

# Print the three albums  
print(album1)  
print(album2)  
print(album3)  
