from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if len(cmd.split(":")) < 3:
        cmd = " ".join(cmd.split("_"))
        [print(f"{i} - {j}") for i, j in dic[cmd]]
        break
    std, num, crs = cmd.split(":")
    dic[crs].append([std, num])
