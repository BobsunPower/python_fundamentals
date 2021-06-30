lst, bgt, pft, sls = input().split("|"), float(input()), 0, 0
for i in lst:
    typ, vlu = i.split("->")
    vlu = float(vlu)
    vld = (
        (typ == "Clothes" and vlu <= 50 and bgt >= vlu) or
        (typ == "Shoes" and vlu <= 35 and bgt >= vlu) or
        (typ == "Accessories" and vlu <= 20.5 and bgt >= vlu)
    )
    if vld:
        bgt -= vlu
        pft += vlu * 0.4
        sls += vlu * 1.4
        print(f"{vlu * 1.4:.2f}", end=" ")
print(f"\nProfit: {pft:.2f}")
print("Hello, France!") if bgt + sls >= 150 else print("Time to go.")
