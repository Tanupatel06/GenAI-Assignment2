# Take order_amount as a input from User
try:
    order_amount = int(input("Enter the Order Amount :"))

# Apply discount based on the order_amount
    if order_amount >=2000:
        print("You Get 15% Discount :", (order_amount*15)/100)
        print("Total Amount After Discount :", order_amount - (order_amount*15)/100)
    elif order_amount >=1500 and order_amount <2000:
        print("You Get 10% Discount :", (order_amount*10)/100)
        print("Total Amount After Discount :", order_amount - (order_amount*10)/100)
    elif order_amount >=1000 and order_amount <1500:
        print("You Get 5% Discount :", (order_amount*5)/100)
        print("Total Amount After Discount :", order_amount - (order_amount*5)/100)
    else:
        print("0 % Discount Available")
        print("Total Amount After Discount :", order_amount)
    
# Handle ValueError if user enters a non-numeric value
except ValueError:
    print("Invalid input! Please enter a numeric value for the order amount.")
  
# Calculate tax amount based on the total amount after discount   
print("Tax Amount : 5% of Total Amount After Discount ")
tax_amount = (order_amount - (order_amount * 0.05)) * 0.05
print("Tax Amount :", tax_amount)
print("Sub Total Amount After Tax :", (order_amount - (order_amount * 0.05)) + tax_amount)


    

    