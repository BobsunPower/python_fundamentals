from collections import defaultdict
dic = defaultdict(list)
while True:
    cmd = input()
    if cmd == "end":
        break
    crs, std = cmd.split(" : ")
    dic[crs].append(std)
out = []
for crs, students in sorted(dic.items(), key=lambda x: -len(x[1])):
    out.append(f'{crs}: {len(students)}')
    [out.append(f'-- {std}') for std in sorted(students)]
print('\n'.join(out))
