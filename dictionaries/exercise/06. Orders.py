dic = {}
while True:
    cmd = input()
    if cmd == "buy":
        print("\n".join(f"{i} -> {j['price'] * j['quantity']:.2f}" for i, j in dic.items()))
        break
    pdt, prz, qty = cmd.split()
    if pdt not in dic:
        dic[pdt] = {"price": float(prz), "quantity": int(qty)}
        continue
    dic[pdt]['price'] = float(prz)
    dic[pdt]["quantity"] += int(qty)
