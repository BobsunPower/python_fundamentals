import re
pat = r'(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})'
[print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}") for i in re.findall(pat, input())]
