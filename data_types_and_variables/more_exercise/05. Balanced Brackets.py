lines = int(input())
parentheses = []
balanced = True
last_symbol = ''
for x in range(lines):
    symbol = input()
    if symbol == '(' and last_symbol == '(':
        balanced = False
        break
    parentheses.append(symbol)
    if symbol == "(" or symbol == ")":
        last_symbol = symbol
if parentheses.count('(') == parentheses.count(')') and balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
