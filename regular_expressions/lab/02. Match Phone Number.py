import re
pat = r'(\+359([- ])2\2\d{3}\2\d{4}\b)'
print(', '.join([p for p, _ in re.findall(pat, input())]))
