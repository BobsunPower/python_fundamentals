n = int(input())
stds = {}
out = {}
for _ in range(n):
    name = input()
    grd = float(input())
    if name not in stds:
        stds[name] = []
    stds[name].append(grd)
for name, grd in stds.items():
    res = sum(grd) / len(grd)
    if res >= 4.5:
        out[name] = res
for name, res in sorted(out.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {res:.2f}")
