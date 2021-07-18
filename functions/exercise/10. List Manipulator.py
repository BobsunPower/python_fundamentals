def exchange(arr, i):
    if 0 <= i < len(arr):
        return arr[i + 1:] + arr[:i + 1]
    print('Invalid index')


def max_even(arr):
    evn_num = -1
    evn_idx = -1
    for i in range(len(arr)):
        if arr[i] >= evn_num and arr[i] % 2 == 0:
            evn_num = arr[i]
            evn_idx = i
    if evn_idx >= 0:
        print(evn_idx)
    else:
        print("No matches")


def max_odd(arr):
    odd_num = -1
    odd_idx = -1
    for i in range(len(arr)):
        if arr[i] >= odd_num and arr[i] % 2 == 1:
            odd_num = arr[i]
            odd_idx = i
    if odd_idx >= 0:
        print(odd_idx)
    else:
        print("No matches")


def min_even(arr):
    evn_num = 1001
    evn_idx = 1001
    for i in range(len(arr)):
        if arr[i] <= evn_num and arr[i] % 2 == 0:
            evn_num = arr[i]
            evn_idx = i
    if evn_idx < 1001:
        print(evn_idx)
    else:
        print("No matches")


def min_odd(arr):
    odd_num = 1001
    odd_idx = 1001
    for i in range(len(arr)):
        if arr[i] <= odd_num and arr[i] % 2 == 1:
            odd_num = arr[i]
            odd_idx = i
    if odd_idx < 1001:
        print(odd_idx)
    else:
        print("No matches")


lst = list(map(int, input().split()))
while True:
    cmd = input().split()
    if cmd[0] == "end":
        break
    if cmd[0] == "exchange":
        idx = int(cmd[1])
        lst = exchange(lst, idx)
    elif cmd[0] == "max":
        if cmd[1] == "even":
            max_even(lst)
        elif cmd[1] == "odd":
            max_odd(lst)
    elif cmd[0] == "min":
        if cmd[1] == "even":
            min_even(lst)
        elif cmd[1] == "odd":
            min_odd(lst)
