rng, cap, tnk = int(input()), 255, 0
for i in range(rng):
    wtr = int(input())
    if wtr > cap:
        print("Insufficient capacity!")
        continue
    tnk += wtr
    cap -= wtr
print(tnk)
