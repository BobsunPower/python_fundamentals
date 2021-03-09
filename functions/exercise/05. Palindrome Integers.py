def palindrome_finder():
    lst = input().split(", ")
    for i in lst:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


palindrome_finder()
