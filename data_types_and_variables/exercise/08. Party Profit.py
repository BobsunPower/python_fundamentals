crew = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    coins += 50
    if day % 10 == 0:
        crew -= 2
    if day % 15 == 0:
        crew += 5
    coins -= crew * 2
    if day % 3 == 0:
        coins -= crew * 3
    if day % 5 == 0:
        coins += crew * 20
        if day % 3 == 0:
            coins -= crew * 2
print(f"{crew} companions received {int(coins / crew)} coins each.")
