age = 31  # Define the age variable

# Check if the age is less than 21
if age < 21:
    print("milk")  # If age is less than 21, print "milk"

# Check if the age is between 21 and 79 (inclusive of 21 but less than 80)
elif age >= 21 and age < 80:
    print("beer")  # If age is between 21 and 79, print "beer"

# If none of the above conditions are met (age is 80 or above)
else:
    print("prune juice")  # If age is 80 or above, print "prune juice"
