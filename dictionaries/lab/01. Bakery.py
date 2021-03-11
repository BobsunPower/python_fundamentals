data = input().split()
print({data[i]: int(data[i + 1]) for i in range(0, len(data), 2)})
