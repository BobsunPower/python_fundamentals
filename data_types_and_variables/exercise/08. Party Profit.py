ppl, dys, cns = int(input()), int(input()), 0
for d in range(1, dys + 1):
    if d % 10 == 0:
        ppl -= 2
    if d % 15 == 0:
        ppl += 5
        cns -= ppl * 2
    cns += 50 - (ppl * 2)
    if d % 3 == 0:
        cns -= ppl * 3
    if d % 5 == 0:
        cns += ppl * 20
print(f"{ppl} companions received {(cns // ppl)} coins each.")
