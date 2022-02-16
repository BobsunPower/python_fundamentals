import re
pat = r'\b_([a-zA-Z0-9]+)\b'
print(",".join([m for m in re.findall(pat, input())]))
