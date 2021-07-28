from collections import defaultdict
wds, dic = input().split(), defaultdict(int)
for i in wds:
    dic[i.lower()] += 1
print(" ".join([i for i, j in dic.items() if j % 2 == 1]))
