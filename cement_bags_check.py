from datetime import datetime

# Function to check if a cement bag is defective
def check_cement_bag(weight, is_wet, expiration_date):
    issues = []

    # Check if weight is within acceptable range (48 to 52 kg)
    acceptable_range = (48, 52)
    if not (acceptable_range[0] <= weight <= acceptable_range[1]):
        issues.append("Unacceptable weight")

    # Check if the bag is wet
    if is_wet:
        issues.append("The bag is wet")

    # Check if the expiration date has passed
    today = datetime.today().date()
    try:
        expiry = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        if expiry < today:
            issues.append("Expired")
    except ValueError:
        # Handle invalid date format
        issues.append("Invalid expiration date format")

    # Return result based on any issues found
    if issues:
        return f"Defective bag: {', '.join(issues)}"
    else:
        return "The bag is OK"

# Example usage: List of cement bags (weight, is_wet, expiration_date)
bags = [
    (49.5, False, "2025-06-01"),       # Good bag
    (53.0, False, "2025-06-01"),       # Overweight
    (50.0, True, "2025-06-01"),        # Wet bag
    (50.0, False, "2024-04-01"),       # Expired
    (47.0, True, "bad-date")           # Underweight, wet, and invalid date
]

# Check each bag and print result
for i, bag in enumerate(bags, 1):
    print(f"Bag {i}: {check_cement_bag(*bag)}")
