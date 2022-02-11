fst, sec = input().split()
out = 0
for i in range(min(len(fst), len(sec))):
    out += ord(fst[i]) * ord(sec[i])
if len(fst) > len(sec):
    for i in fst[len(sec):]:
        out += ord(i)
elif len(fst) < len(sec):
    for i in sec[len(fst):]:
        out += ord(i)
print(out)
