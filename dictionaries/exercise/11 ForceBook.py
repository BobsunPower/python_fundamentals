# Reworked version. 100 Judge pts.
dic_frs, dic_usr = {}, {}
while True:
    cmd = input()
    if cmd == 'Lumpawaroo':
        break
    elif '|' in cmd:
        frs, usr = cmd.split(' | ')
        if usr not in dic_usr:
            dic_usr[usr] = frs
            if frs not in dic_frs:
                dic_frs[frs] = [usr]
            else:
                dic_frs[frs].append(usr)
    else:
        usr, frs = cmd.split(' -> ')
        if usr in dic_usr:
            dic_frs[dic_usr[usr]].remove(usr)
            dic_usr[usr] = frs
            if frs in dic_frs:
                dic_frs[frs].append(usr)
            else:
                dic_frs[frs] = [usr]
        else:
            if frs in dic_frs:
                dic_usr[usr] = frs
                dic_frs[frs].append(usr)
            else:
                dic_frs[frs] = [usr]
        print(f"{usr} joins the {frs} side!")
for k, v in dic_frs.items():
    if len(v):
        print(f"Side: {k}, Members: {len(v)}")
        for u in v:
            print(f'! {u}')
# My style version. 80/100 Judge pts.
# from collections import defaultdict
# dic, frs, usr = defaultdict(list), None, None
# while True:
#     cmd = input()
#     if cmd == "Lumpawaroo":
#         break
#     if " | " in cmd:
#         frs, usr = cmd.split(" | ")
#         if [usr] not in dic.values():
#             dic[frs].append(usr)
#     else:
#         usr, frs = cmd.split(" -> ")
#         if [usr] in dic.values():
#             dic = {k: v for k, v in dic.items() if v != [usr]}
#         dic[frs].append(usr)
#         print(f"{usr} joins the {frs} side!")
# for f in dic:
#     print(f"Side: {f}, Members: {len(dic[f])}")
#     [print(f"! {u}") for u in dic[f]]
