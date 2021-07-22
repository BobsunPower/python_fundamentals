lst = input().split()
for i in lst:
    msg = list(chr(int("".join([j for j in i if j.isdigit()])))) + [j for j in i if j.isalpha()]
    msg[1], msg[-1] = msg[-1], msg[1]
    print("".join(msg), end=" ")
