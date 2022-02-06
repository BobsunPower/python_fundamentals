dic = {}
while True:
    cmd = input()
    if cmd == "buy":
        [print(f"{k} -> {v['mny'] * v['qty']:.2f}") for k, v in dic.items()]
        break
    buy, mny, qty = cmd.split()
    if buy not in dic:
        dic[buy] = {"mny": float(mny), "qty": int(qty)}
    else:
        dic[buy]['mny'] = float(mny)
        dic[buy]['qty'] += int(qty)
