def calculate_ticket_prices():
    # Get user inputs
    age = input("Enter age (adult/child/senior):").lower()
    day = input("Enter day of the week (weekday/weekend):").lower()
    num_tickets = int(input("Enter the number of tickets:"))
    is_Group = input("Is it a group booking? (yes/no):").lower()=="yes"
    is_family = input("Is it is a family package? (yes/no):").lower()=="yes"

    # Determine base price based on age
    if age == "adult":
        base_price = 12.5
    elif age == "child":
        base_price = 8.0
    elif age == "senior":
        base_price = 10.0
    else:
        print("Invalid age input.")
        return
    
    # Apply weekend or weekday pricing
    if day in ["weekday","weekend"]:
        if day == "weekend":
            base_price *= 1.2   # weekend pricing is 20% higher
    else:
        print("Invalid day input.")
        return
    
    # Apply discounts for groups or family packages
    if is_Group:
        base_price *= 0.9 # 10% discount for groups
    elif is_family:
        base_price *= 0.8 # 20% discount for family packages

    # Calculate total price for the given number of tickets
    total_price = base_price * num_tickets

    print(f"Total tickets price: ${total_price:.2f}")

# Call the function to calculate ticket price based on user input
calculate_ticket_prices()