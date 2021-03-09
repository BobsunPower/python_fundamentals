herd = input().split(", ")
sheep = len(herd)
if herd[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for wolf in herd:
        sheep -= 1
        if wolf == "wolf":
            print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
            break
