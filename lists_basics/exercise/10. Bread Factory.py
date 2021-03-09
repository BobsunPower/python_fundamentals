lst = input().split("|")
energy = 100
coins = 100
bankrupt = False
for i in lst:
    order, n = i.split("-")
    n = int(n)
    if order == "rest":
        if energy + n <= 100:
            energy += n
            print(f"You gained {n} energy.")
        else:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")
    elif order == "order":
        if energy >= 30:
            coins += n
            energy -= 30
            print(f"You earned {n} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= n
        if coins > 0:
            print(f"You bought {order}.")
        else:
            bankrupt = True
            print(f"Closed! Cannot afford {order}.")
            break
if not bankrupt:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
