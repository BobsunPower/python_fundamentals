from collections import defaultdict
dic = defaultdict(int)
while True:
    cmd = input()
    if cmd == "stop":
        print("\n".join(f"{i} -> {j}" for i, j in dic.items()))
        break
    dic[cmd] += int(input())
