from collections import defaultdict
from statistics import mean
dic, out, std = defaultdict(list), defaultdict(list), None
for i in range(int(input())):
    std, grd = input(), float(input())
    dic[std].append(grd)
for i, j in dic.items():
    if mean(j) >= 4.5:
        out[i] = mean(j)
[print(f"{i} -> {j:.2f}") for i, j in sorted(out.items(), key=lambda x: x[1], reverse=True)]
