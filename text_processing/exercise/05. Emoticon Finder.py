txt = input()
[print(f"{txt[i]}{txt[i + 1]}") for i, j in enumerate(txt) if j == ":"]
