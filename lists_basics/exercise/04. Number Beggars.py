lst = list(map(int, input().split(", ")))
bgs = [0 for _ in range(int(input()))]
for i in range(len(lst)):
    bgs[i % len(bgs)] += lst[i]
print(bgs)
