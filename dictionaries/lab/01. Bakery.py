lst = input().split()
print({lst[i]: int(lst[i + 1]) for i in range(0, len(lst), 2)})
