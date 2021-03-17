subj = {}
while True:
    cmd = input()
    if cmd == "end":
        break
    crs, std = cmd.split(" : ")
    if crs not in subj:
        subj[crs] = [std]
    else:
        subj[crs].append(std)
out = []
for crs, students in sorted(subj.items(), key=lambda x: -len(x[1])):
    out.append(f'{crs}: {len(students)}')
    for std in sorted(students):
        out.append(f'-- {std}')
print('\n'.join(out))
