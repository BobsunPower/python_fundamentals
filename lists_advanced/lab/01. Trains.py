train = [0] * int(input())
while True:
    cmd = input().split()
    if cmd[0] == "End":
        break
    if cmd[0] == "add":
        train[-1] += int(cmd[1])
    elif cmd[0] == "insert":
        train[int(cmd[1])] += int(cmd[2])
    elif cmd[0] == "leave":
        train[int(cmd[1])] -= int(cmd[2])
print(train)
