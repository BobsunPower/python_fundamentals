lst = input().split()
shuffles = int(input())
half = len(lst) // 2
output = []
for _ in range(shuffles):
    output = []
    for i in range(half):
        output.append(lst[i])
        output.append(lst[half + i])
    lst = output
print(output)
