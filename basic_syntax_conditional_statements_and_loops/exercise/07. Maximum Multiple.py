d = int(input())
b = int(input())
for i in range(b, -1, -1):
    if i % d == 0:
        print(i)
        break
