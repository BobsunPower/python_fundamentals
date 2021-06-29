lst, shl, out = input().split(), int(input()), []
for _ in range(shl):
    out = []
    for i in range(len(lst) // 2):
        out.append(lst[i])
        out.append(lst[len(lst) // 2 + i])
    lst = out
print(out)
