lst = [0] * int(input())
while True:
    cmd = input().split()
    if cmd[0] == "End":
        print(lst)
        break
    if cmd[0] == "add":
        lst[-1] += int(cmd[1])
    if cmd[0] == "insert":
        lst[int(cmd[1])] += int(cmd[2])
    if cmd[0] == "leave":
        lst[int(cmd[1])] -= int(cmd[2])
