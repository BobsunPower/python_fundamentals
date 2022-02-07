from collections import defaultdict
dic = defaultdict(list)
for i in range(int(input())):
    dic[input()].append(float(input()))
[print(f"{k} -> {sum(v) / len(v):.2f}") for k, v in dic.items() if sum(v) / len(v) >= 4.5]
