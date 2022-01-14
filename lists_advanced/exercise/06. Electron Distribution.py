els, lst, fac = int(input()), [], 0
while els > 0:
    fac += 1
    vlu = 2 * fac ** 2
    lst.append(vlu) if vlu <= els else lst.append(els)
    els -= vlu
print(lst)
