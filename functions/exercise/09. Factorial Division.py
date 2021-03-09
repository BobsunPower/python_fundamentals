from math import factorial


def factorial_and_divide(number, divisor):
    print(f"{(factorial(number) / factorial(divisor)):.2f}")


factorial_and_divide(int(input()), int(input()))
