num_lst = input().split()
str_lst = list(input())
idx = []
for num in num_lst:
    num_sum = 0
    for dgt in num:
        num_sum += int(dgt)
    idx.append(num_sum)
msg = []
for i in idx:
    if i > len(str_lst):
        i -= len(str_lst)
    msg.append(str_lst.pop(i))
print("".join(msg))
