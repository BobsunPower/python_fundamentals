s, i, r, o = input(), 0, "", ""
while i < len(s):
    if s[i].isdigit():
        n = s[i]
        if i + 1 < len(s) and s[i + 1].isdigit():
            n += s[i + 1]
            i += 1
        m = int(n)
        o += r * m
        r = ""
    else:
        r += s[i].upper()
    i += 1
print(f"Unique symbols used: {len(set(o))}\n{o}")
