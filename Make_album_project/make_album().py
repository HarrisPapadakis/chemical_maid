import make_album


while True:
    print("\nEnter artist and album title (or type 'q' to quit):")  # Prompt the user to enter details
    artist = input("Artist: ")  # Get the artist's name from user input
    if artist.lower() == "q":  # Check if the user wants to quit the loop
        break

    title = input("Album title: ")  # Get the album title from user input
    if title.lower() == "q":  # Check if the user wants to quit the loop
        break

    album = make_album(artist, title)  # Call the function to create an album dictionary
    print(f"Album created: {album}")  # Display the created album dictionary
