d, b = int(input()), int(input())
for i in range(b, d, -1):
    if i % d == 0:
        print(i)
        break
