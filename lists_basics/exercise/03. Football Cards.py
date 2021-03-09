lst = input().split()
a = 11
b = 11
terminated = False
for i in set(lst):
    lst.append(i)
    if "A" in i:
        a -= 1
    else:
        b -= 1
    if a < 7 or b < 7:
        terminated = True
        break
print(f"Team A - {a}; Team B - {b}")
if terminated:
    print("Game was terminated")
