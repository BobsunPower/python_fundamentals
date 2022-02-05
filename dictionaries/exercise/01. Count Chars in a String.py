lst = [ch for ch in input() if not ch.isspace()]
dic = {ch: lst.count(ch)for ch in lst}
[print(f"{k} -> {v}") for k, v in dic.items()]
