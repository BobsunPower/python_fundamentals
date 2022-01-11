lst = []
while True:
    cmd = input().split("-")
    if cmd[0] == "End":
        print([act for i, act in sorted(lst)])
        break
    lst.append([int(cmd[0]), cmd[1]])
