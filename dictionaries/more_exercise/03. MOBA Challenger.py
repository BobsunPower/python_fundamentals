from collections import defaultdict
players = defaultdict(dict)
while True:
    data = input()
    if data == 'Season end':
        break
    if ' -> ' in data:
        player, position, skill = data.split(' -> ')
        skill = int(skill)
        new = True
        for p in players:
            if p == player:
                for pos, skl in players[p].items():
                    if pos == position:
                        new = False
                        if skl < skill:
                            players[player][position] = skill
        if new:
            players[player][position] = skill
    elif " vs " in data:
        fst_plr, sec_plr = data.split(" vs ")
        found = False
        if fst_plr in players and sec_plr in players:
            for fst_pos, fst_skl in players[fst_plr].items():
                for sec_pos, sec_skl in players[sec_plr].items():
                    if fst_pos == sec_pos:
                        found = True
                        fst_plr_res = sum(players[fst_plr].values())
                        sec_plr_res = sum(players[sec_plr].values())
                        if fst_plr_res > sec_plr_res:
                            players.pop(sec_plr)
                        elif fst_plr_res < sec_plr_res:
                            players.pop(fst_plr)
                    if found:
                        break
                if found:
                    break
for plr in sorted(players, key=lambda x: -sum(players[x].values())):
    tot = sum(players[plr].values())
    print(f"{plr}: {tot} skill")
    for pos, skl in sorted(players[plr].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {skl}")
