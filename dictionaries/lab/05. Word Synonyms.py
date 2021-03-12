from collections import defaultdict

syn_dic = defaultdict(list)
n = int(input())
for _ in range(n):
    wrd = input()
    syn = input()
    syn_dic[wrd].append(syn)
for wrd, syn_dic in syn_dic.items():
    sys = ", ".join(syn_dic)
    print(f"{wrd} - {sys}")
