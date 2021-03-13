from collections import defaultdict
ch_el_dic = defaultdict(int)
while True:
    cmd = input()
    if cmd == "stop":
        break
    tkn = cmd
    vlu = int(input())
    ch_el_dic[tkn] += vlu
for i, j in ch_el_dic.items():
    print(f"{i} -> {j}")
