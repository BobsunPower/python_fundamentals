rms = int(input())
fr_ch = 0
for rm in range(rms):
    ch, ppl = input().split()
    ch = int(len(ch))
    ppl = int(ppl)
    rm = rm + 1
    if ch >= ppl:
        free = ch - ppl
        fr_ch += free
    else:
        free = ppl - ch
        fr_ch -= free
        print(f"{ppl - ch} more chairs needed in room {rm}")
if fr_ch >= 0:
    print(f"Game On, {fr_ch} free chairs left")
