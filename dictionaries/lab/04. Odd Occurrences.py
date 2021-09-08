from collections import defaultdict
lst, dic = input().split(), defaultdict(int)
for i in lst:
    dic[i.lower()] += 1
print(" ".join([i for i, j in dic.items() if j % 2 == 1]))
