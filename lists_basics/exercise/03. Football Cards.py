lst, a, b = list(set(input().split())), 11, 11
for i in range(len(lst)):
    if "A" in lst[0]:
        a -= 1
    else:
        b -= 1
    lst.pop(0)
    if a < 7 or b < 7:
        break
print(f"Team A - {a}; Team B - {b}")
if a < 7 or b < 7:
    print("Game was terminated")
