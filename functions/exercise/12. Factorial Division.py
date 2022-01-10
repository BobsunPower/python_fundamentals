from math import factorial


def factorial_division(n, d):
    print(f"{(factorial(n) / factorial(d)):.2f}")


factorial_division(int(input()), int(input()))
