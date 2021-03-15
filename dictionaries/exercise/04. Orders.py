goods = {}
while True:
    data = input()
    if data == 'buy':
        break
    name, price, qty = data.split(' ')
    price, qty = float(price), int(qty)
    if name not in goods:
        goods[name] = {'price': price, 'quantity': qty}
    else:
        goods[name]['quantity'] += qty
        if goods[name]['price'] != price:
            goods[name]['price'] = price
for k, v in goods.items():
    total = v['price'] * v['quantity']
    print(f'{k} -> {total:.2f}')
