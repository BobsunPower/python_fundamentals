from collections import defaultdict
leg = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
res, jnk = {'shards': 0, 'fragments': 0, 'motes': 0}, defaultdict(int)
while True:
    itm, qty = [], []
    [qty.append(int(j)) if i % 2 == 0 else itm.append(j) for i, j in enumerate(input().lower().split())]
    for k, v in zip(itm, qty):
        if k in res:
            res[k] += v
            if res[k] >= 250:
                print(f'{leg[k]} obtained!')
                res[k] -= 250
                [print(f"{k}: {v}") for k, v in res.items()]
                [print(f"{k}: {v}") for k, v in jnk.items()]
                exit()
        else:
            jnk[k] += v
