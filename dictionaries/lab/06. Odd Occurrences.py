lst = input().lower().split()
dic = {crs: lst.count(crs)for crs in lst}
print(" ".join([k for k, v in dic.items() if v % 2 == 1]))
