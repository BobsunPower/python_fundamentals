string = input()
lst = []
i = 0
for c in string:
    if c.isupper() is True:
        lst.append(i)
    i += 1
print(lst)
