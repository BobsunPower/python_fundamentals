stat = {}
ind_stat = {}
while True:
    data = input()
    if data == "no more time":
        break
    user, con, pts = data.split(" -> ")
    pts = int(pts)
    if con not in stat:
        stat[con] = {}
    if user not in stat[con]:
        stat[con][user] = pts
    else:
        if pts > stat[con][user]:
            stat[con][user] = pts
for con, stat in stat.items():
    print(f"{con}: {len(stat)} participants")
    sort = dict(sorted(stat.items(), key=lambda x: (-x[1], x[0])))
    pos = 1
    for name, pts in sort.items():
        print(f"{pos}. {name} <::> {pts}")
        pos += 1
    for k, v in stat.items():
        if k not in ind_stat:
            ind_stat[k] = 0
        ind_stat[k] += v
print("Individual standings:")
pos = 1
for user, tot_pts in sorted(ind_stat.items(), key=lambda x: (-x[1], x[0])):
    print(f"{pos}. {user} -> {tot_pts}")
    pos += 1
