from collections import defaultdict
dic = defaultdict(int)
while True:
    cmd = input()
    if cmd == "statistics":
        break
    key, qty = cmd.split(": ")
    dic[key] += int(qty)
print(f"Products in stock:"), [print(f"- {k}: {v}") for k, v in dic.items()]
print(f"Total Products: {len(dic)}\nTotal Quantity: {sum(dic.values())}")
