from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if cmd == "end":
        break
    crs, std = cmd.split(" : ")
    dic[crs].append(std)
for c in dic:
    print(f"{c}: {len(dic[c])}")
    [print(f"-- {s}") for s in dic[c]]
