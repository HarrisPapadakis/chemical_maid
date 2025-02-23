def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""  
    full_name = f"{first_name} {last_name}"  # Create a full name string with proper spacing
    return full_name.title()  # Convert the full name to title case and return it

# Infinite loop to continuously ask for user input
while True:  
    print("\nPlease tell me your name:")
    print('(Enter "q" at any time to quit)')  # Provide instructions for quitting

    # Get first name input from the user
    f_name = input("First name: ")  
    if f_name.lower() == "q":  # Convert input to lowercase to allow both 'q' and 'Q' to exit
        break  

    # Get last name input from the user
    l_name = input("Last name: ")  # Prompt for last name input
    if l_name.lower() == "q":  # Check if user wants to quit
        break  

    # Call the function to format the name
    formatted_name = get_formatted_name(f_name, l_name)  
    print(f"\nHello, {formatted_name}!")  # Display a greeting with the formatted name
