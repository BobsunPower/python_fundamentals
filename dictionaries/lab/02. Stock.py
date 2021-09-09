lst, sch = input().split(), input().split()
dic = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
[print(f"We have {dic[i]} of {i} left") if i in dic else print(f"Sorry, we don't have {i}") for i in sch]
