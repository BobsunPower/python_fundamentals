lst = input().split()
while True:
    order = input().split()
    if "Money" in order:
        break
    if "OutOfStock" in order:
        lst = ["None" if lst[i] == order[1] else lst[i] for i in range(len(lst))]
    elif "Required" in order:
        lst = [order[1] if i == int(order[2]) else lst[i] for i in range(len(lst))]
    elif "JustInCase" in order:
        lst = [order[1] if lst[i] == lst[-1] else lst[i] for i in range(len(lst))]
lst = [lst[i] for i in range(len(lst)) if not lst[i] == "None"]
print(" ".join([str(i) for i in lst]))
