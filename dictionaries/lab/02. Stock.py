lst, sch, pdt, qty = input().split(), input().split(), [], []
[pdt.append(j) if i % 2 == 0 else qty.append(int(j)) for i, j in enumerate(lst)]
dic = {k: v for k, v in zip(pdt, qty)}
[print(f"We have {dic[i]} of {i} left") if i in dic else print(f"Sorry, we don't have {i}") for i in sch]
