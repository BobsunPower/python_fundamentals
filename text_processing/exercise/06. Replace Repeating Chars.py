s = input()
[print(s[i], end="") for i in range(len(s)) if i + 1 == len(s) or s[i] != s[i + 1]]
