from collections import defaultdict
dic = defaultdict(list)
[dic[input()].append(input()) for i in range(int(input()))]
[print(f"{k} - {', '.join(v)}") for k, v in dic.items()]
