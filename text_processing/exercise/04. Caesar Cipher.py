def caesar(txt: str):
    out = ''
    for c in txt:
        out += chr(ord(c) + 3)
    return out


text = input()
print(caesar(text))
