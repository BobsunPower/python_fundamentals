def password_validator(pas):
    dgt, alp = len([1 for i in pas if i.isdigit()]), len([1 for i in pas if i.isalpha()])
    if 6 <= len(pas) <= 10 and len(pas) == alp + dgt and dgt >= 2:
        return print("Password is valid")
    if not 6 <= len(pas) <= 10:
        print("Password must be between 6 and 10 characters")
    if not len(pas) == alp + dgt:
        print("Password must consist only of letters and digits")
    if dgt < 2:
        print("Password must have at least 2 digits")


password_validator(input())
