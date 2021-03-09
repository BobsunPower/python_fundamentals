lst = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    lst.remove(min(lst))
print(lst)
