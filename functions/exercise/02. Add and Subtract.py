def add_and_subtract(x, y, z):
    def sum_numbers():
        return x + y

    def subtract():
        return sum_numbers() - z

    return subtract()


print(add_and_subtract(int(input()), int(input()), int(input())))
