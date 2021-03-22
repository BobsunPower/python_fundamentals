ban, txt = input().split(", "), input()
for wrd in ban:
    if wrd in txt:
        txt = txt.replace(wrd, "*" * len(wrd))
print(txt)
