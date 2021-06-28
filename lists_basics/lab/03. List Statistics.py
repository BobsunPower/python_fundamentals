rng, pos, neg = int(input()), [], []
for _ in range(rng):
    n = int(input())
    pos.append(n) if n >= 0 else neg.append(n)
print(f"{pos}\n{neg}\nCount of positives: {len(pos)}. Sum of negatives: {sum(neg)}")
