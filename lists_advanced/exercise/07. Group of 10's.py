from math import ceil

lst = list(map(int, input().split(", ")))
[print(f"Group of {i + 1}0's: {[j for j in lst if i * 10 < j <= (i + 1) * 10]}") for i in range((ceil(max(lst) / 10)))]
