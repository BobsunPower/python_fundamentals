def calculations(act, x, y):
    if act == "multiply":
        return x * y
    if act == "divide":
        return x // y
    if act == "add":
        return x + y
    if act == "subtract":
        return x - y


print(calculations(input(), int(input()), int(input())))
