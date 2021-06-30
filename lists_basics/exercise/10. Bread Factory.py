lst, nrg, cns = input().split("|"), 100, 100
for i in lst:
    order, vlu = i.split("-")
    vlu = int(vlu)
    if order == "rest":
        if nrg + vlu <= 100:
            nrg += vlu
            print(f"You gained {vlu} energy.")
        else:
            print(f"You gained {100 - nrg} energy.")
            nrg = 100
        print(f"Current energy: {nrg}.")
    elif order == "order":
        if nrg >= 30:
            cns += vlu
            nrg -= 30
            print(f"You earned {vlu} coins.")
        else:
            nrg += 50
            print("You had to rest!")
    else:
        cns -= vlu
        if cns > 0:
            print(f"You bought {order}.")
        else:
            print(f"Closed! Cannot afford {order}.")
            exit()
print(f"Day completed!\nCoins: {cns}\nEnergy: {nrg}")
