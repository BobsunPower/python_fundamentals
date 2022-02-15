import re
pat = r'((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s)))'
[print(n[0], end=' ') for n in re.findall(pat, input())]
