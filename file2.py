def calculate_total_bill():
    # Get user inputs for order items, quantities,and prices
    order_items = input("Enter order items (comma-separated): ").split(',')
    quantities = [int(qty) for qty in input("Enter quantities (comma-separated): ").split(',')]
    prices = [float(prices) for prices in input("Enter prices (comma-separated): ").split(',')]

    # Check if the lengths of order_items, quantities and prices are consistent
    if len(order_items) != len(quantities) or len(order_items) != len(prices):
        print("Invalid input lengths.")
        return

    # Calculate total bill amount
    total_bill = sum(qty*prices for qty,prices in zip(quantities,prices))

    # Apply discounts
    apply_discount = input("Apply discount? (yes/no): ").lower() =="yes"
    if apply_discount:
        discount_percentage = float(input("Enter discount percentage: "))
        total_bill *= (100 - discount_percentage)/100

    # Apply taxes
    apply_tax = input("Apply tax? (yes/no): ").lower() == "yes"
    if apply_tax:
        tax_percentage = float(input("Enter tax percentage:"))
        total_bill *= (100 + tax_percentage) / 100

    # Split the bill among friends
    split_bill = input("split the bill among friends? (yes/no): ").lower() == "yes"
    if split_bill:
        num_friends = int(input("Enter the number of friends: "))
        total_bill /= num_friends + 1 # Including yourself 

    print(f"Total bill among: ${total_bill:.2f}")

# Call the function to calculate the total bill based on user input
calculate_total_bill()                                        