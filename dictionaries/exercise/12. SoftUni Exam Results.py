from collections import defaultdict
dic_exm, dic_sts, ban = defaultdict(int), {}, []
while True:
    cmd = input()
    if cmd == "exam finished":
        break
    if "banned" in cmd.split("-"):
        ban.append(cmd.split("-")[0])
        continue
    std, lng, pts = cmd.split("-")
    dic_exm[lng] += 1
    dic_sts[std] = max(dic_sts.get(std, 0), int(pts))
print("Results:"), [print(f"{k} | {v}") for k, v in dic_sts.items() if k not in ban]
print("Submissions:"), [print(f"{k} - {v}") for k, v in dic_exm.items()]
