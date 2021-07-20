lst = input().split()
palindrome = input()
print(f"{[i for i in lst if i == i[::-1]]}\nFound palindrome {lst.count(palindrome)} times")
