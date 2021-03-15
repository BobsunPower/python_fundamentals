n = int(input())
park = {}
for _ in range(n):
    cmd = input().split()
    name = cmd[1]
    if cmd[0] == "register":
        reg_num = cmd[2]
        if name in park:
            print(f"ERROR: already registered with plate number {reg_num}")
        else:
            park[name] = reg_num
            print(f"{name} registered {reg_num} successfully")
    elif cmd[0] == "unregister":
        if name not in park:
            print(f'ERROR: user {name} not found')
        else:
            print(f'{name} unregistered successfully')
            del park[name]
print('\n'.join([f'{k} => {v}' for k, v in park.items()]))
