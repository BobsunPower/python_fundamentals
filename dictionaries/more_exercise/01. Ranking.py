from collections import defaultdict
val = {}
contests = defaultdict(list)
while True:
    data = input()
    if data == 'end of contests':
        break
    con, pas = data.split(':')
    val[con] = pas
while True:
    data = input()
    if data == 'end of submissions':
        break
    con, pas, user, pts = data.split('=>')
    pts = int(pts)
    if con in val:
        if val[con] == pas:
            if user not in contests:
                contests[user].append(
                    {'contest': con, 'points': pts})
            else:
                new_con = True
                for i in range(len(contests[user])):
                    c = contests[user][i]['contest']
                    p = contests[user][i]['points']
                    if c == con:
                        new_con = False
                        if p < pts:
                            contests[user][i]['points'] = pts
                        break
                if new_con:
                    contests[user].append({'contest': con, 'points': pts})
tot_pts = defaultdict(int)
for user, data in contests.items():
    for i in range(len(data)):
        tot_pts[user] += contests[user][i]['points']
for user, pts in tot_pts.items():
    if pts == max(tot_pts.values()):
        print(f'Best candidate is {user} with total {pts} points.')
print('Ranking:')
for user, data in sorted(contests.items()):
    print(user)
    for res in sorted(data, key=lambda x: -x['points']):
        con = res['contest']
        pts = res['points']
        print(f'#  {con} -> {pts}')
