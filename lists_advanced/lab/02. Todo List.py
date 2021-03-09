todo_lst = []
while True:
    cmd = input().split("-")
    if cmd[0] == "End":
        break
    todo_lst.append((int(cmd[0]), cmd[1]))
print([task for idx, task in sorted(todo_lst)])
