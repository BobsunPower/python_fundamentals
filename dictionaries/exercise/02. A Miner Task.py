from collections import defaultdict
dic = defaultdict(int)
while True:
    cmd = input()
    if cmd == "stop":
        for i, j in dic.items():
            print(f"{i} -> {j}")
        break
    dic[cmd] += int(input())
