from math import factorial


def factorial_division(num, dvd):
    print(f"{(factorial(num) / factorial(dvd)):.2f}")


factorial_division(int(input()), int(input()))
