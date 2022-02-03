from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if len(cmd.split(":")) < 3:
        [print(f"{k} - {v}") for k, v in dic[" ".join(cmd.split("_"))]]
        break
    std, num, crs = cmd.split(":")
    dic[crs].append([std, num])
