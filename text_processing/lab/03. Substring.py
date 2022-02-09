prt, txt = input(), input()
while prt in txt:
    txt = txt.replace(prt, "")
print(txt)
