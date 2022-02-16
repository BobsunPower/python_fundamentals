import re
pat = r'\d+'
while True:
    txt = input()
    if not txt:
        break
    [print(d, end=" ") for d in re.findall(pat, txt)]
