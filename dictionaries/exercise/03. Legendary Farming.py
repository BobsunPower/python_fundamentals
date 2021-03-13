from collections import defaultdict
REQUIRED_COMPONENTS = 250
items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
components = {'shards': 0, 'fragments': 0, 'motes': 0}
useless_items = defaultdict(int)
while True:
    assembled = False
    data = input().split(' ')
    for i in range(0, len(data), 2):
        material = data[i + 1].lower()
        quantity = int(data[i])
        if material in components:
            components[material] += quantity
            if components[material] >= REQUIRED_COMPONENTS:
                print(f'{items[material]} obtained!')
                components[material] -= REQUIRED_COMPONENTS
                assembled = True
                break
        else:
            useless_items[material] += quantity
    if assembled:
        break
for material, quantity in sorted(components.items(), key=lambda x: (-x[1], x[0])):
    print(f'{material}: {quantity}')
for material, quantity in sorted(useless_items.items(), key=lambda x: x[0]):
    print(f'{material}: {quantity}')
