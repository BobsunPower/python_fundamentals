lst = input().split("#")
lst = [i.split(" = ") for i in lst]
wtr, eft, fir = int(input()), 0, 0
print("Cells:")
for i in range(len(lst)):
    lvl, vlu = lst[i][0], int(lst[i][1])
    vld = (
        (lvl == "High" and vlu in range(81, 126) and wtr >= vlu) or
        (lvl == "Medium" and vlu in range(51, 81) and wtr >= vlu) or
        (lvl == "Low" and vlu in range(1, 51) and wtr >= vlu)
    )
    if vld:
        wtr -= vlu
        eft += vlu * 0.25
        fir += vlu
        print(f" - {vlu}")
print(f"Effort: {eft:.2f}\nTotal Fire: {fir}")
