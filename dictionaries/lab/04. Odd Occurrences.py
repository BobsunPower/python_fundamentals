from collections import defaultdict

txt_lst = input().lower().split()
txt_dic = defaultdict(int)
for i in txt_lst:
    txt_dic[i] += 1
print(" ".join([i for i, j in txt_dic.items() if j % 2 == 1]))
