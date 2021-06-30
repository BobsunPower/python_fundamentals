def orders(itm, qty):
    if itm == "coffee":
        return f"{1.5 * qty:.2f}"
    elif itm == "water":
        return f"{qty:.2f}"
    elif itm == "coke":
        return f"{1.4 * qty:.2f}"
    elif itm == "snacks":
        return f"{2 * qty:.2f}"


print(orders(input(), int(input())))
