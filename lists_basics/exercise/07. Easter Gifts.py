lst = input().split()
while True:
    cmd = input().split()
    if "Money" in cmd:
        break
    if "OutOfStock" in cmd:
        lst = ["None" if lst[i] == cmd[1] else lst[i] for i in range(len(lst))]
    elif "Required" in cmd:
        lst = [cmd[1] if i == int(cmd[2]) else lst[i] for i in range(len(lst))]
    elif "JustInCase" in cmd:
        lst[-1] = cmd[1]
lst = [lst[i] for i in range(len(lst)) if not lst[i] == "None"]
print(" ".join(lst))
