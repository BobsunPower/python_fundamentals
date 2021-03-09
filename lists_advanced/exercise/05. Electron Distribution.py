electrons = int(input())
output = []
idx = 1
while electrons > 0:
    cell = 2 * idx ** 2
    el_left = electrons - cell
    if electrons >= cell:
        output.append(cell)
    else:
        output.append(cell + el_left)
    electrons = el_left
    idx += 1
print(output)
