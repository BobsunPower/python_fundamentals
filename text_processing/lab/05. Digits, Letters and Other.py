txt = input()
dgt, ltr, otr = "", "", ""
for ch in txt:
    if ch.isdigit():
        dgt += ch
    elif ch.isalpha():
        ltr += ch
    else:
        otr += ch
print(dgt, ltr, otr, sep='\n')
