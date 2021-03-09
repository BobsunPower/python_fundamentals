first = input()
second = input()
merge = ""
last = first
for a in range(len(first)):
    for b in range(a + 1):
        merge += second[b]
    for c in range(a + 1, len(first)):
        merge += first[c]
    if merge != last:
        print(merge)
        last = merge
    merge = ""
