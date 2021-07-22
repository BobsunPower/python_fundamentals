lst = input().split(", ")
while True:
    cmd = input().split(" - ")
    if cmd[0] == "Craft!":
        break
    act, itm = cmd[0], cmd[1]
    if act == "Collect":
        itm not in lst and lst.append(itm)
    elif act == "Drop":
        itm in lst and lst.remove(itm)
    elif act == "Combine Items":
        old, new = itm.split(":")
        old in lst and lst.insert(lst.index(old) + 1, new)
    elif act == "Renew":
        if itm in lst:
            lst.remove(itm)
            lst.append(itm)
print(", ".join(lst))
