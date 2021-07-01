def characters_in_range(x, y):
    return " ".join([chr(i) for i in range(ord(x) + 1, ord(y))])


print(characters_in_range(input(), input()))
