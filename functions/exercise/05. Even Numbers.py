def even_numbers(x):
    return x % 2 == 0


print(list(filter(even_numbers, [int(i) for i in input().split()])))
