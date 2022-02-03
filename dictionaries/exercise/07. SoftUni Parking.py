dic = {}
for _ in range(int(input())):
    cmd = input().split()
    usr = cmd[1]
    if cmd[0] == "register":
        if usr in dic:
            print(f"ERROR: already registered with plate number {cmd[2]}")
            continue
        dic[usr] = cmd[2]
        print(f"{usr} registered {cmd[2]} successfully")
    elif cmd[0] == "unregister":
        if usr not in dic:
            print(f'ERROR: user {usr} not found')
            continue
        print(f'{usr} unregistered successfully')
        del dic[usr]
print('\n'.join([f'{k} => {v}' for k, v in dic.items()]))
