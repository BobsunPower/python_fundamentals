from collections import defaultdict
dic = defaultdict(int)
while True:
    cmd = input()
    if cmd == "stop":
        break
    dic[cmd] += int(input())
[print(f"{k} -> {v}")for k, v in dic.items()]
