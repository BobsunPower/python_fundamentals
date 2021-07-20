lst = []
while True:
    cmd = input().split("-")
    if cmd[0] == "End":
        break
    lst.append((int(cmd[0]), cmd[1]))
print([t for i, t in sorted(lst)])
