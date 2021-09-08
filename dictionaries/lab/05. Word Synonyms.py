from collections import defaultdict
dic = defaultdict(list)
[dic[input()].append(input()) for i in range(int(input()))]
for i, j in dic.items():
    print(f"{i} - {', '.join(j)}")
