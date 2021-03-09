lst = list(map(int, input().split("@")))
idx = 0
val_day = 0
while True:
    cmd = [int(ch) if ch.isdigit() else str(ch) for ch in input().split()]
    if "Love!" in cmd:
        break
    else:
        length = cmd[1]
        idx += length
        if idx > len(lst) - 1:
            idx = 0
        if lst[idx] == 0:
            print(f"Place {idx} already had Valentine's day.")
        else:
            lst[idx] -= 2
            if lst[idx] == 0:
                print(f"Place {idx} has Valentine's day.")
                val_day += 1
print(f"Cupid's last position was {idx}.")
if val_day == len(lst):
    print('Mission was successful.')
else:
    no_val = len(lst) - val_day
    print(f'Cupid has failed {no_val} places.')
