dic = {}
for i in range(int(input())):
    cmd = input().split()
    usr = cmd[1]
    if len(cmd) == 3:
        if usr not in dic:
            dic[usr] = cmd[2]
            print(f"{usr} registered {cmd[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {cmd[2]}")
    else:
        if usr in dic:
            del dic[usr]
            print(f"{usr} unregistered successfully")
        else:
            print(f"ERROR: user {usr} not found")
[print(f"{k} => {v}") for k, v in dic.items()]
