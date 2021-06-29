lst = list(map(int, input().split()))
[lst.remove(min(lst)) for _ in range(int(input()))]
for i in range(len(lst)):
    print(lst[i], end="")
    if not i == len(lst) - 1:
        print(", ", end="")
