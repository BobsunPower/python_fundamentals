eng, lft = True, 0
for i in range(1, int(input()) + 1):
    chs, ppl = input().split()
    chs, ppl = len(chs), int(ppl)
    if chs < ppl:
        print(f"{ppl - chs} more chairs needed in room {i}")
        eng = False
    else:
        lft += chs - ppl
if eng:
    print(f"Game On, {lft} free chairs left")
