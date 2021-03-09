inv = input().split(", ")
while True:
    cmd = input().split(" - ")
    if cmd[0] == "Craft!":
        break
    act = cmd[0]
    itm = cmd[1]
    if act == "Collect":
        if itm not in inv:
            inv.append(itm)
    elif act == "Drop":
        if itm in inv:
            inv.remove(itm)
    elif act == "Combine Items":
        old, new = itm.split(":")
        if old in inv:
            pos = inv.index(old) + 1
            inv.insert(pos, new)
    elif act == "Renew":
        if itm in inv:
            inv.remove(itm)
            inv.append(itm)
print(", ".join(inv))
