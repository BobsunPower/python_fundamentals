from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if len(cmd.split(":")) < 3:
        cmd = " ".join(cmd.split("_"))
        for i in dic[cmd]:
            print(f"{i[0]} - {i[1]}")
        break
    std, num, crs = cmd.split(":")
    dic[crs].append([std, num])
