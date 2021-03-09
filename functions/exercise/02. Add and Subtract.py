def sum_numbers(x, y):
    return x + y


def subtract(x, y):
    return x - y


def add_and_subtract(x, y, z):
    aggregate = sum_numbers(x, y)
    total = subtract(aggregate, z)
    print(total)


add_and_subtract(int(input()), int(input()), int(input()))
