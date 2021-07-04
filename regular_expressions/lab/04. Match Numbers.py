# TODO
import re
pattern = r'(^|(?<=\s))(?P<n>-?\d+(\.[\d]+)?)($|(?=\s))'
data = input()
matches = re.finditer(pattern, data)
numbers = [n.group('n') for n in matches]
print(*numbers)
