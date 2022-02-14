s = input()
[print(f"{s[i]}{s[i + 1]}") for i, j in enumerate(s) if j == ":"]
