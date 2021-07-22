ets, out, fac = int(input()), [], 0
while ets > 0:
    fac += 1
    vlu = 2 * fac ** 2
    if vlu <= ets:
        out.append(vlu)
    else:
        out.append(ets)
    ets -= vlu
print(out)
