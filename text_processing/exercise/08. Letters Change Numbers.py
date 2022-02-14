alp, tot = {chr(97 + i): i + 1 for i in range(26)}, 0
for i in input().split():
    fst, lst = i[0], i[-1]
    num = int(i[1:-1])
    num = num / alp[fst.lower()] if fst.isupper() else num * alp[fst]
    num = num - alp[lst.lower()] if lst.isupper() else num + alp[lst]
    tot += num
print(f"{tot:.2f}")
