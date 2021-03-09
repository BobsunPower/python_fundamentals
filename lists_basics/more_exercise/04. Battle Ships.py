rws = int(input())
sea = [[int(i) for i in input().split()] for _ in range(rws)]
atk_lst = input().split()
dsd = 0
for atk in atk_lst:
    tgt = atk.split("-")
    row = int(tgt[0])
    col = int(tgt[1])
    if sea[row][col] > 0:
        sea[row][col] -= 1
        if sea[row][col] == 0:
            dsd += 1
print(dsd)
