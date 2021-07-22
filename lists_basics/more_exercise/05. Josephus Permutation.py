lst = input().split(' ')
k = int(input())
out = []
ctr = 0
idx = 0
while len(lst) > 0:
    ctr += 1
    if ctr % k == 0:
        out.append(lst.pop(idx))
    else:
        idx += 1
    if idx >= len(lst):
        idx = 0
print(str(out).replace(' ', '').replace('\'', ''))
