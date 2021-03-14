goods = {}
while True:
    data = input()
    if data == 'buy':
        break
    name, price, quantity = data.split(' ')
    price = float(price)
    quantity = int(quantity)
    if name not in goods:
        goods[name] = {'price': price, 'quantity': quantity}
    else:
        goods[name]['quantity'] += quantity
        if goods[name]['price'] != price:
            goods[name]['price'] = price
for i, j in goods.items():
    total = j['price'] * j['quantity']
    print(f'{i} -> {total:.2f}')
