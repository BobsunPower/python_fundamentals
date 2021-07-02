def add_and_subtract(x, y, z):
    def sum_numbers(a, b):
        return a + b

    def subtract():
        return sum_numbers(x, y) - z

    return subtract()


print(add_and_subtract(int(input()), int(input()), int(input())))
