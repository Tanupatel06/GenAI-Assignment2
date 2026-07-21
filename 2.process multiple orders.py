# List of Orders
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order\tDiscount\tFinal Amount")
print("--------------------------------")

# Used a for loop to iterate through the list of orders and calculate the discount and final amount for each order
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

    total_revenue += final_amount

    if discount > 0:
        discounted_orders += 1

print("--------------------------------")
print("Total Revenue After Discount =", total_revenue)
print("Orders Received Discount =", discounted_orders)