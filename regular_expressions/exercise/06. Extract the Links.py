import re
pat = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))'
while True:
    cmd = input()
    if not cmd:
        break
    for m in re.finditer(pat, cmd):
        print(m.group())
