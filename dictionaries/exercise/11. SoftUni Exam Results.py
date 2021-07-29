out = {}
sub = {}
while True:
    data = input()
    if data == "exam finished":
        break
    data = data.split("-")
    if len(data) == 3:
        std, lng, res = data[0], data[1], int(data[2])
        if std not in out:
            out[std] = res
        if out[std] < res:
            out[std] = res
        if lng not in sub:
            sub[lng] = 1
        else:
            sub[lng] += 1
    else:
        std = data[0]
        del out[std]
print("Results:")
for std, res in sorted(out.items(), key=lambda x: (-x[1], x[0])):
    print(f"{std} | {res}")
print("Submissions:")
for lng, num in sorted(sub.items()):
    print(f"{lng} - {num}")
