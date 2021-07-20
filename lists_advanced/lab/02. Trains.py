lst = [0] * int(input())
while True:
    cmd = input().split()
    if cmd[0] == "End":
        break
    if cmd[0] == "add":
        lst[-1] += int(cmd[1])
    elif cmd[0] == "insert":
        lst[int(cmd[1])] += int(cmd[2])
    elif cmd[0] == "leave":
        lst[int(cmd[1])] -= int(cmd[2])
print(lst)
