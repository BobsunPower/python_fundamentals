rng, pos, neg = int(input()), [], []
for _ in range(rng):
    n = int(input())
    if n > 0:
        pos.append(n)
    else:
        neg.append(n)
print(f"{pos}\n{neg}\nCount of positives: {len(pos)}. Sum of negatives: {sum(neg)}")
