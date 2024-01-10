def estimate_travel_cost():
    # Get the user input for destination, travel style and duration
    destination = input("Enter the destination: ")
    travel_style = input("Choose travel style (budget/luxury): ").lower()
    duration = int(input("Enter the duration of the trip (in days): "))

    # Set default cost values
    transportation_cost = 0
    accommodation_cost = 0
    activites_cost = 0

    # Define cost factors based on travel style
    if travel_style == "budget":
        transportation_cost = 50  # Budget transporatation cost per day
        accommodation_cost = 70   # Budget accommodation cost per day
        activites_cost = 30   # Budget activites cost per day
    elif travel_style == "luxury":
        transportation_cost = 150  # luxury transporatation cost per day
        accommodation_cost = 200   # luxury accommodation cost per day
        activites_cost = 100    # luxury activites cost per day
    else:
        print("Invalid travel style.")
        return 
    
    # Calculate total travel cost
    total_cost = (transportation_cost + accommodation_cost + activites_cost) * duration

    # Display results
    print(f"Estimated travel cost for {duration} days in {destination} ({travel_style} style): ${total_cost:.2f}")

# Call the function to estimate travel cost based on user input
estimate_travel_cost()