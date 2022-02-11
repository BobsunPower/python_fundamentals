dgs, lts, ors = "", "", ""
for i in input():
    if i.isdigit():
        dgs += i
    elif i.isalpha():
        lts += i
    else:
        ors += i
print(dgs, lts, ors, sep="\n")
