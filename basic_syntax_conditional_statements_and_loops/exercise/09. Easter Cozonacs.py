budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk = flour * 1.25 * 0.25
cake = flour + eggs + milk
easter_eggs = 0
cakes = 0
while budget > cake:
    budget -= cake
    easter_eggs += 3
    cakes += 1
    if cakes % 3 == 0:
        easter_eggs -= cakes - 2
print(f"You made {cakes} cozonacs! Now you have {easter_eggs} eggs and {budget:.2f}BGN left.")
