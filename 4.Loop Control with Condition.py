# List daily sales data 
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

# if the sale = -1, it indicates corrupted data and the loop will break
# else if the sale = 0, it indicates no sales for that day and the loop will continue to the next iteration
# else, the sale amount will be added to the total_sales and the running total will be printed
for sale in daily:
    if sale == -1:
        print("Corrupted Data Found!")
        break
    if sale == 0:
        print("No Sales Today.")
        continue

    total_sales += sale
    print("Added:", sale, "Running Total:", total_sales)

print("---------------------------")
print("Final Total Sales =", total_sales)