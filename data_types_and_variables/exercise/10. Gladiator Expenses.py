lst, hlm, swd, shd, arm, exp = int(input()), float(input()), float(input()), float(input()), float(input()), 0
for lss in range(1, lst + 1):
    if lss % 2 == 0:
        exp += hlm
    if lss % 3 == 0:
        exp += swd
    if lss % 6 == 0:
        exp += shd
    if lss % 12 == 0:
        exp += arm
print(f"Gladiator expenses: {exp:.2f} aureus")
