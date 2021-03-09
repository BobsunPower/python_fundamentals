from math import ceil

int_lst = list(map(int, input().split(',')))
for i in range(ceil(max(int_lst) / 10)):
    grp = [num for num in int_lst if i * 10 < num <= (i + 1) * 10]
    print(f"Group of {(i + 1) * 10}'s: {grp}")
