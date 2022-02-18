import re
pat = r'\d+'
while True:
    cmd = input()
    if not cmd:
        break
    [print(d, end=" ") for d in re.findall(pat, cmd)]
