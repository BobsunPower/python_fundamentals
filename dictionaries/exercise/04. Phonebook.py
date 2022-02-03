from collections import defaultdict
dic, sch = defaultdict(list), 0
while True:
    cmd = input()
    if cmd.isdigit():
        sch = int(cmd)
        break
    key, num = cmd.split("-")
    if key in dic:
        dic[key] = num
        continue
    dic[key].append(num)
for i in range(sch):
    psn = input()
    print(f"{psn} -> {''.join(dic[psn])}") if psn in dic else print(f"Contact {psn} does not exist.")
