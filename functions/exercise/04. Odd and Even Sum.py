def odd_and_even_sum(n):
    return f"Odd sum = {sum([int(i) for i in n if int(i) % 2 == 1])}, \
Even sum = {sum([int(i) for i in n if int(i) % 2 == 0])}"


print(odd_and_even_sum(input()))
