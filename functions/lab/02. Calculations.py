def calculations(act, x, y):
    if act == "multiply":
        return x * y
    elif act == "divide":
        return x // y
    elif act == "add":
        return x + y
    elif act == "subtract":
        return x - y


print(calculations(input(), int(input()), int(input())))
