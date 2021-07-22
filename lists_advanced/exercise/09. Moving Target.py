lst = list(map(int, input().split()))
while True:
    cmd = input().split()
    if cmd[0] == "End":
        break
    idx, vlu = int(cmd[1]), int(cmd[2])
    if cmd[0] == "Shoot":
        if 0 <= idx < len(lst):
            lst[idx] -= vlu
            lst.remove(lst[idx]) if lst[idx] < 1 else lst[idx]
    elif cmd[0] == "Add":
        if 0 <= idx < len(lst):
            lst.insert(idx, vlu)
        else:
            print("Invalid placement!")
    elif cmd[0] == "Strike":
        if idx + vlu < len(lst) and idx - vlu >= 0:
            del lst[idx - vlu:idx + vlu + 1]
        else:
            print("Strike missed!")
print("|".join([str(i) for i in lst]))
