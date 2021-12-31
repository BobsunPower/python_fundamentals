def characters_in_range(fst, lst):
    return [chr(i) for i in range(ord(fst) + 1, ord(lst))]


print(" ".join(characters_in_range(input(), input())))
