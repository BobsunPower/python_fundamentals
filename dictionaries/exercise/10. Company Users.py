from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if cmd == "End":
        break
    com, emp = cmd.split(" -> ")
    if emp in dic[com]:
        continue
    dic[com].append(emp)
for c in dic:
    print(f"{c}")
    [print(f"-- {e}") for e in dic[c]]
