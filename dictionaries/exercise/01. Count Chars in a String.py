from collections import defaultdict

txt_lst = input()
txt_dic = defaultdict(int)
for i in txt_lst:
    if i == " ":
        continue
    txt_dic[i] += 1
for i, j in txt_dic.items():
    print(f"{i} -> {j}")
