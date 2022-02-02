lst, pdt, qty = input().split(), [], []
[pdt.append(j) if i % 2 == 0 else qty.append(int(j)) for i, j in enumerate(lst)]
print({k: v for k, v in zip(pdt, qty)})
