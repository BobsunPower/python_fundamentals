fst = input().split()
sec = input().split()
trd = input().split()
wnr = ""
if fst[0] == fst[1] == fst[2]:
    wnr = fst[0]
elif sec[0] == sec[1] == sec[2]:
    wnr = sec[0]
elif trd[0] == trd[1] == trd[2]:
    wnr = sec[0]
elif fst[0] == sec[0] == trd[0]:
    wnr = fst[0]
elif fst[1] == sec[1] == trd[1]:
    wnr = fst[1]
elif fst[2] == sec[2] == trd[2]:
    wnr = fst[2]
elif fst[0] == sec[1] == trd[2]:
    wnr = fst[0]
elif fst[2] == sec[1] == trd[0]:
    wnr = fst[0]
if wnr == "1":
    print("First player won")
elif wnr == "2":
    print("Second player won")
else:
    print("Draw!")
