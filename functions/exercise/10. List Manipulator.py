def exchange(arr, idx):
    if idx <= -1 or idx >= len(arr):
        print("Invalid index")
        return arr
    arr = arr[idx + 1:] + arr[:idx + 1]
    return arr


def max_even(arr):
    fnd, idx, evn = False, None, 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            fnd = True
            if arr[i] >= evn:
                evn = arr[i]
                idx = i
    if not fnd:
        return "No matches"
    else:
        return idx


def max_odd(arr):
    fnd, idx, odd = False, None, 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            fnd = True
            if arr[i] >= odd:
                odd = arr[i]
                idx = i
    if not fnd:
        return "No matches"
    else:
        return idx


def min_even(arr):
    fnd, idx, evn = False, None, 1001
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            fnd = True
            if arr[i] <= evn:
                evn = arr[i]
                idx = i
    if not fnd:
        return "No matches"
    else:
        return idx


def min_odd(arr):
    fnd, idx, odd = False, None, 1001
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            fnd = True
            if arr[i] <= odd:
                odd = arr[i]
                idx = i
    if not fnd:
        return "No matches"
    else:
        return idx


def first_even(arr, cnt):
    out = []
    if cnt > len(arr) or cnt <= 0:
        return "Invalid count"
    for num in arr:
        if num % 2 == 0 and cnt > 0:
            out.append(num)
            cnt -= 1
    return out


def first_odd(arr, cnt):
    out = []
    if cnt > len(arr) or cnt <= 0:
        return "Invalid count"
    for num in arr:
        if num % 2 != 0 and cnt > 0:
            out.append(num)
            cnt -= 1
    return out


def last_even(arr, cnt):
    out = []
    if cnt > len(arr) or cnt <= 0:
        return "Invalid count"
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0 and cnt > 0:
            out.append(arr[i])
            cnt -= 1
    return out[::-1]


def last_odd(arr, cnt):
    out = []
    if cnt > len(arr) or cnt <= 0:
        return "Invalid count"
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 != 0 and cnt > 0:
            out.append(arr[i])
            cnt -= 1
    return out[::-1]


def list_manipulator():
    lst = list(map(int, input().split()))

    while True:
        cmd = input().split()
        if cmd[0] == "end":
            print(lst)
            break
        elif cmd[0] == "exchange":
            lst = exchange(lst, int(cmd[1]))
        elif cmd[0] == "max":
            if cmd[1] == "even":
                print(max_even(lst))
            elif cmd[1] == "odd":
                print(max_odd(lst))
        elif cmd[0] == "min":
            if cmd[1] == "even":
                print(min_even(lst))
            elif cmd[1] == "odd":
                print(min_odd(lst))
        elif cmd[0] == "first":
            if cmd[2] == "even":
                print(first_even(lst, int(cmd[1])))
            elif cmd[2] == "odd":
                print(first_odd(lst, int(cmd[1])))
        elif cmd[0] == "last":
            if cmd[2] == "even":
                print(last_even(lst, int(cmd[1])))
            elif cmd[2] == "odd":
                print(last_odd(lst, int(cmd[1])))


list_manipulator()
