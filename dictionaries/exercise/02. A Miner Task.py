from collections import defaultdict
chem_el = defaultdict(int)
while True:
    cmd = input()
    if cmd == "stop":
        break
    vlu = int(input())
    chem_el[cmd] += vlu
for k, v in chem_el.items():
    print(f"{k} -> {v}")
