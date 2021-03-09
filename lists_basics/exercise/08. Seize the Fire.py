lst = input().split("#")
lst = [i.split(" = ") for i in lst]
water = int(input())
effort = 0
fire = 0
cells = []
valid = False
for i in range(len(lst)):
    level = lst[i][0]
    value = int(lst[i][1])
    valid = (
        (level == "High" and 81 <= value <= 126) or
        (level == "Medium" and 51 <= value <= 80) or
        (level == "Low" and 1 <= value <= 50)
    )
    if valid and water >= value:
        water -= value
        effort += value * 0.25
        fire += value
        cells.append(value)
print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\nTotal Fire: {fire}")
