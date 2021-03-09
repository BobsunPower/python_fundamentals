flows = int(input())
capacity = 255
tank = 0
for i in range(flows):
    water = int(input())
    if water > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= water
    tank += water
print(tank)
