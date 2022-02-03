from collections import defaultdict
lst, dic = input().lower().split(), defaultdict(int)
for k in lst:
    dic[k] += 1
print(" ".join([k for k, v in dic.items() if v % 2 == 1]))
