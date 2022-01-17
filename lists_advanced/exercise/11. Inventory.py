lst = input().split(", ")
while True:
    cmd = input()
    if cmd == "Craft!":
        print(", ".join([str(i) for i in lst]))
        break
    act, itm = cmd.split(" - ")
    if act == "Collect" and itm not in lst:
        lst.append(itm)
    elif act == "Drop" and itm in lst:
        lst.remove(itm)
    elif act == "Combine Items":
        old, new = itm.split(":")
        old in lst and lst.insert(lst.index(old) + 1, new)
    elif act == "Renew" and itm in lst:
        lst.append(lst.pop(lst.index(itm)))
