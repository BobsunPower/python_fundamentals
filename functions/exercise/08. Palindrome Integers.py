def palindrome_integers(txt):
    lst = txt.split(", ")
    out = ["True" if i == i[::-1] else "False" for i in lst]
    return print("\n".join([i for i in out]))


palindrome_integers(input())
