def calculate_price(stock, quantity):
    if stock == "coffee":
        return quantity * 1.5
    if stock == "water":
        return quantity * 1
    if stock == "coke":
        return quantity * 1.4
    if stock == "snacks":
        return quantity * 2


price = calculate_price(input(), int(input()))
print(f"{price:.2f}")
