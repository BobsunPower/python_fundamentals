import re
txt, pat = input(), rf'\b{input()}\b'
print(len([i for i in re.findall(pat, txt, re.IGNORECASE)]))
