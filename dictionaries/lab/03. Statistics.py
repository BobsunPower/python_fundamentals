from collections import defaultdict
dic = defaultdict(int)
while True:
    cmd = input().split(": ")
    if cmd[0] == "statistics":
        break
    itm, qty = cmd[0], int(cmd[1])
    dic[itm] += int(qty)
print("Products in stock:"), [print(f"- {i}: {j}") for i, j in dic.items()]
print(f"Total Products: {len(dic)}\nTotal Quantity: {sum(dic.values())}")
