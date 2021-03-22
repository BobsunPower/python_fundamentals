left, right = input().split()
tot = 0
for i in range(min(len(left), len(right))):
    lft_ord = ord(left[i])
    rgt_ord = ord(right[i])
    tot += lft_ord * rgt_ord
if len(left) > len(right):
    rest = left[len(right):]
    for vlu in rest:
        tot += ord(vlu)
elif len(left) < len(right):
    rest = right[len(left):]
    for vlu in rest:
        tot += ord(vlu)
print(tot)
