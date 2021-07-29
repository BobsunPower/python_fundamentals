from collections import defaultdict
txt, dic = input(), defaultdict(int)
for i in txt:
    if not i.isspace():
        dic[i] += 1
print("\n".join(f"{i} -> {j}" for i, j in dic.items()))
