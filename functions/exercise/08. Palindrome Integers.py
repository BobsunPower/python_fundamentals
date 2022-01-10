def palindrome_integers(lst):
    [print("True") if i == i[::-1] else print("False") for i in lst]


palindrome_integers(input().split(", "))
