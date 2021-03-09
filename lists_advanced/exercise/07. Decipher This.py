code = input().split(" ")
for wrd in code:
    decipher = []
    char = [ch for ch in wrd if ch.isdigit()]
    char = chr(int("".join(char)))
    decipher += char
    second = [alpha for alpha in wrd if alpha.isalpha()]
    decipher += second
    decipher[1], decipher[-1] = decipher[-1], decipher[1]
    print("".join(decipher), end=" ")
