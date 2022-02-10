lst, txt = input().split(", "), input()
for ban in lst:
    while ban in txt:
        txt = txt.replace(ban, len(ban) * "*")
print(txt)
