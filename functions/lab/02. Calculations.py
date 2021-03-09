def calculate(action, x, y):
    if action == "multiply":
        return x * y
    if action == "divide":
        return x // y
    if action == "add":
        return x + y
    if action == "subtract":
        return x - y


print(calculate(input(), int(input()), int(input())))
