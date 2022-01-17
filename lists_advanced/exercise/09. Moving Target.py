lst = list(map(int, input().split()))
while True:
    cmd = input().split()
    if cmd[0] == "End":
        print("|".join([str(i) for i in lst]))
        break
    act, idx, vlu = cmd[0], int(cmd[1]), int(cmd[2])
    if act == "Shoot":
        if 0 <= idx < len(lst):
            lst[idx] -= vlu
            lst.remove(lst[idx]) if lst[idx] < 1 else lst[idx]
    elif act == "Add":
        lst.insert(idx, vlu) if 0 <= idx < len(lst) else print("Invalid placement!")
    elif act == "Strike":
        if idx + vlu < len(lst) and idx - vlu >= 0:
            del lst[idx - vlu:idx + vlu + 1]
        else:
            print("Strike missed!")
