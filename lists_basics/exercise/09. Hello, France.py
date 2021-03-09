lst = input().split("|")
budget = float(input())
sales = []
profit = []
for i in lst:
    item, price = i.split("->")
    price = float(price)
    if budget >= price:
        if item == 'Clothes' and price <= 50.00 \
                or item == 'Shoes' and price <= 35.00 \
                or item == 'Accessories' and price <= 20.50:
            sales.append(price * 1.4)
            profit.append(price * 0.4)
            budget -= price
for j in sales:
    print(f"{j:.2f}", end=" ")
print(f"\nProfit: {sum(profit):.2f}")
if budget + sum(sales) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
