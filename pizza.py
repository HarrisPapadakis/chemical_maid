def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    # The asterisk (*) before 'toppings' allows the function to accept multiple arguments as a tuple
    print(toppings)  # Print the tuple containing all the toppings provided

# Call the function with a single topping
make_pizza("pepperoni")

# Call the function with multiple toppings
make_pizza("mushrooms", "green peppers", "extra cheese")
