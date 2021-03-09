lst = list(map(int, input().split(", ")))
beggars = int(input())
output = [0] * beggars
for i in range(len(lst)):
    output[i % beggars] += lst[i]
print(output)
