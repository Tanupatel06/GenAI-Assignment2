# Take List of order_amount as input from User and apply discount based on the order_amount
orders =[]

# Menu driven program to add order amounts and view orders with discounts
while True:
    print("\n ==========MENU==========")
    print("1. Add Order Amount")
    print("2. View Orders and Discounts")
    print("q. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            order_amount = int(input("Enter the Order Amount: "))
            orders.append(order_amount)
            print("Order amount added successfully.")
        except ValueError:
            print("Invalid input! Please enter a numeric value for the order amount.")
    
    elif choice == '2':
        if len(orders) == 0:
            print("No orders available.")
            continue
        total = 0
        discounted_orders = 0
        print("\nOrder\tDiscount\tFinal Amount")
        print("--------------------------------")
        for amount in orders:
            if amount >= 3000:
                discount = 20
            elif amount >= 2000:
                discount = 15
            elif amount >= 1000:
                discount = 10
            else:
                discount = 0

            discount_amount = amount * discount / 100
            final_amount = amount - discount_amount

            print(amount, "\t", str(discount) + "%", "\t\t", final_amount)

            total += final_amount

            if discount > 0:
                discounted_orders += 1

        print("\nTotal Final Amount: ", total)
        print("Number of Discounted Orders: ", discounted_orders)
        
    # Handle the quit option and invalid choices
    elif choice == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please select a valid option from the menu.")
        continue