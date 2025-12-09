sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sale_on_w2_last_day = input("Enter sales on last day of week 2: ")

sales_w2.append(int(sale_on_w2_last_day))

print(f"Sale of Week 1 : {sales_w1}")
print(f"Sale of Week 2 : {sales_w2}")

# Total Sales
sales = sales_w1 +sales_w2
sales.sort()
print(sales)


worst_profit = min(sales)*1.5 
print(f"Worst profit: {worst_profit}")

best_profit =max(sales)*1.5
print(f"Best profit: {best_profit}")

print(f"Combined profit: {worst_profit + best_profit}")