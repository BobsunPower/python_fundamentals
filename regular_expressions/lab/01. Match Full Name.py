import re
pat = r'(\b[A-Z][a-z]+ [A-Z][a-z]+\b)'
print(' '.join(re.findall(pat, input())))
