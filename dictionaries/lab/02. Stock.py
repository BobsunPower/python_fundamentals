data = input().split()
goods = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
lst = input().split()
for itm in lst:
    if itm in goods:
        vlu = goods[itm],
        print(f"We have {vlu} of {itm} left")
    else:
        print(f"Sorry, we don't have {itm}")
