rng = int(input())
snow, time, qty, vlu = 0, 0, 0, 0
for i in range(rng):
    s, t, q = int(input()), int(input()), int(input())
    if (s / t) ** q > vlu:
        vlu = ((s // t) ** q)
        snow, time, qty = s, t, q
print(f"{snow} : {time} = {vlu} ({qty})")
