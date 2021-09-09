from collections import defaultdict
dic = defaultdict(list)
[dic[input()].append(input()) for i in range(int(input()))]
[print(f"{i} - {', '.join(j)}") for i, j in dic.items()]
