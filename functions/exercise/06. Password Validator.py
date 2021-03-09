def check_password(password):
    length = 6 <= len(password) <= 10
    digits = 0
    letters = 0
    for i in password:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
    if length and len(password) == digits + letters and digits >= 2:
        print("Password is valid")
    if not length:
        print("Password must be between 6 and 10 characters")
    if not len(password) == digits + letters:
        print("Password must consist only of letters and digits")
    if not digits >= 2:
        print("Password must have at least 2 digits")


check_password(input())
