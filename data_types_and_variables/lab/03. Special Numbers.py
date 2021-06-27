rng = int(input())
for n in range(1, rng + 1):
    tot = 0
    for dgt in str(n):
        tot += int(dgt)
    spl = tot in (5, 7, 11)
    print(f"{n} -> {spl}")
