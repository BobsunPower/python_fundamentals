from collections import defaultdict
from statistics import mean
dic, out, std = defaultdict(list), defaultdict(list), None
for i in range(int(input())):
    std, grd = input(), float(input())
    dic[std].append(grd)
[out[std].append(mean(i)) for i in dic.values() if mean(i) >= 4.5]
[print(f"{name} -> {mean(res):.2f}") for name, res in sorted(out.items(), key=lambda x: x[1], reverse=True)]

