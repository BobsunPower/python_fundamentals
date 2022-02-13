txt, pwr, i = input(), 0, 0
while i < len(txt):
    if txt[i] == ">":
        pwr += int(txt[i + 1])
    else:
        if pwr > 0:
            txt = txt[:i] + txt[i + 1:]
            pwr -= 1
            i -= 1
    i += 1
print(txt)
