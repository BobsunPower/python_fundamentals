def orders(pdt, qty):
    if pdt == "coffee":
        return f"{1.5 * qty: .2f}"
    if pdt == "water":
        return f"{qty:.2f}"
    if pdt == "coke":
        return f"{1.4 * qty:.2f}"
    if pdt == "snacks":
        return f"{2 * qty:.2f}"


print(orders(input(), int(input())))
