n = int(input())
for i in range(1, n + 1):
    total = 0
    for d in str(i):
        total += int(d)
    special = total == 5 or total == 7 or total == 11
    print(f"{i} -> {special}")
