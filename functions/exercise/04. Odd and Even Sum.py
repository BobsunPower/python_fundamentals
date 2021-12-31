def odd_and_even_sum(num):
    return f"Odd sum = {sum([int(i) for i in num if int(i) % 2 == 1])}, \
Even sum = {sum([int(i) for i in num if int(i) % 2 == 0])}"


print(odd_and_even_sum(input()))
