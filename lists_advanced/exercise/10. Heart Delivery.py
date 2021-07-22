lst, vtn, i = list(map(int, input().split("@"))), 0, 0
while True:
    cmd = input().split()
    if cmd[0] == "Love!":
        break
    i += int(cmd[1])
    i = 0 if i >= len(lst) else i
    lst[i] -= 2
    if lst[i] < 0:
        print(f"Place {i} already had Valentine's day.")
    if lst[i] == 0:
        print(f"Place {i} has Valentine's day.")
        vtn += 1
print(f"Cupid's last position was {i}.")
if len(lst) == vtn:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(lst) - vtn} places.")
