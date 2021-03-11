def exchange(lst, idx):
    if idx <= -1 or idx >= len(lst):
        print("Invalid index")
        return lst
    lst = lst[idx + 1:] + lst[:idx + 1]
    return lst


def max_even(lst):
    found = False
    idx = None
    max_even_num = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            found = True
            if lst[i] >= max_even_num:
                max_even_num = lst[i]
                idx = i
    if not found:
        return "No matches"
    else:
        return idx


def max_odd(lst):
    found = False
    idx = None
    max_odd_num = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            found = True
            if lst[i] >= max_odd_num:
                max_odd_num = lst[i]
                idx = i
    if not found:
        return "No matches"
    else:
        return idx


def min_even(lst):
    found = False
    idx = None
    min_even_num = 1001
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            found = True
            if lst[i] <= min_even_num:
                min_even_num = lst[i]
                idx = i
    if not found:
        return "No matches"
    else:
        return idx


def min_odd(lst):
    found = False
    idx = None
    min_odd_num = 1001
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            found = True
            if lst[i] <= min_odd_num:
                min_odd_num = lst[i]
                idx = i
    if not found:
        return "No matches"
    else:
        return idx


def first_even(lst, count):
    res = []
    if count > len(lst) or count <= 0:
        return "Invalid count"
    for num in lst:
        if num % 2 == 0 and count > 0:
            res.append(num)
            count -= 1
    return res


def first_odd(lst, count):
    res = []
    if count > len(lst) or count <= 0:
        return "Invalid count"
    for num in lst:
        if num % 2 != 0 and count > 0:
            res.append(num)
            count -= 1
    return res


def last_even(lst, count):
    res = []
    if count > len(lst) or count <= 0:
        return "Invalid count"
    for index in range(len(lst) - 1, -1, -1):
        if lst[index] % 2 == 0 and count > 0:
            res.append(lst[index])
            count -= 1
    res = res[::-1]
    return res


def last_odd(lst, count):
    res = []
    if count > len(lst) or count <= 0:
        return "Invalid count"
    for index in range(len(lst) - 1, -1, -1):
        if lst[index] % 2 != 0 and count > 0:
            res.append(lst[index])
            count -= 1
    res = res[::-1]
    return res


def array_manipulator():
    num_lst = list(map(int, input().split()))
    while True:
        cmd = input().split()
        if cmd[0] == "end":
            print(num_lst)
            break
        elif cmd[0] == "exchange":
            num_lst = exchange(num_lst, int(cmd[1]))
        elif cmd[0] == "rnd":
            if cmd[1] == "even":
                print(max_even(num_lst))
            elif cmd[1] == "odd":
                print(max_odd(num_lst))
        elif cmd[0] == "min":
            if cmd[1] == "even":
                print(min_even(num_lst))
            elif cmd[1] == "odd":
                print(min_odd(num_lst))
        elif cmd[0] == "first":
            if cmd[2] == "even":
                print(first_even(num_lst, int(cmd[1])))
            elif cmd[2] == "odd":
                print(first_odd(num_lst, int(cmd[1])))
        elif cmd[0] == "last":
            if cmd[2] == "even":
                print(last_even(num_lst, int(cmd[1])))
            elif cmd[2] == "odd":
                print(last_odd(num_lst, int(cmd[1])))


array_manipulator()
