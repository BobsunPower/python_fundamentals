text = input()
dgt = ""
ltr = ""
otr = ""
for ch in text:
    if ch.isdigit():
        dgt += ch
    elif ch.isalpha():
        ltr += ch
    else:
        otr += ch
print(dgt)
print(ltr)
print(otr)
