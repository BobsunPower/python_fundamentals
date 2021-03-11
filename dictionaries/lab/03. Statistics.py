goods = {}
while True:
    cmd = input()
    if cmd == "statistics":
        break
    food, qty = cmd.split(": ")
    if food not in goods:
        goods[food] = int(qty)
    else:
        goods[food] += int(qty)
print("Products in stock:")
for food, qty in goods.items():
    print(f"- {food}: {qty}")
print(f"Total Products: {len(goods)}")
print(f"Total Quantity: {sum(goods.values())}")
