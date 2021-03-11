lst = input()
num_lst = [int(i) for i in lst if i.isdigit()]
str_lst = [i for i in lst if not i.isdigit()]
take_list = [n for i, n in enumerate(num_lst) if i % 2 == 0]
skip_list = [n for i, n in enumerate(num_lst) if i % 2 != 0]
res, take, skip, start, rnd = [], 0, 0, 0, 0
while True:
    if rnd == len(take_list):
        break
    rnd += 1
    for j in range(start, (start + take_list[take])):
        if j == len(str_lst):
            break
        res.append(str_lst[j])
    start += take_list[take]
    start += skip_list[skip]
    take += 1
    skip += 1
print(f'{"".join(res)}')
