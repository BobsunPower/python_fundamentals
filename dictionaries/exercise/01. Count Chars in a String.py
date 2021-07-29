from collections import defaultdict
txt, dic = input(), defaultdict(int)
for i in txt:
    if not i.isspace():
        dic[i] += 1
for i, j in dic.items():
    print(f"{i} -> {j}")
