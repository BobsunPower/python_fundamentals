from collections import defaultdict
dic = defaultdict(list)
for i in range(int(input())):
    wrd, syn = input(), input()
    dic[wrd].append(syn)
for i, j in dic.items():
    print(f"{i} - {', '.join(j)}")
