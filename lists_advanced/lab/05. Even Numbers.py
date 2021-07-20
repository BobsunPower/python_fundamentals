lst = list(map(int, (input().split(", "))))
print([i for i, num in enumerate(lst) if num % 2 == 0])
