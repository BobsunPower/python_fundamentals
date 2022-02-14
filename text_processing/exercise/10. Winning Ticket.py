lst, sbs = [i.strip() for i in input().split(",")], ("@", "#", "$", "^")
fnd = lambda x: next(filter(lambda y: y in x, [x * 6 for x in sbs]), None)
for tkt in lst:
    if len(tkt) != 20:
        print("invalid ticket")
        continue
    if fnd(tkt[:10]) and fnd(tkt[10:]):
        c = fnd(tkt[:10])[0]
        if tkt == c * 20:
            print(f'ticket "{tkt}" - 10{c} Jackpot!')
        else:
            for i in range(10, 5, -1):
                if (c * i in tkt[:10]) and (c * i in tkt[10:]):
                    print(f'ticket "{tkt}" - {i}{c}')
                    break
    else:
        print(f'ticket "{tkt}" - no match')
