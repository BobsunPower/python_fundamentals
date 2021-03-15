from collections import defaultdict

txt_lst = input()
txt_dic = defaultdict(int)
for c in txt_lst:
    if c == " ":
        continue
    txt_dic[c] += 1
for k, v in txt_dic.items():
    print(f"{k} -> {v}")
