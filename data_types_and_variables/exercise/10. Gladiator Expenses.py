losses = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armour = float(input())
expenses = 0
for x in range(1, losses + 1):
    if x % 2 == 0:
        expenses += helmet
    if x % 3 == 0:
        expenses += sword
    if x % 6 == 0:
        expenses += shield
    if x % 12 == 0:
        expenses += armour
print(f"Gladiator expenses: {expenses:.2f} aureus")
