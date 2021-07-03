def password_validator(pas):
    vld = True
    dgs = len([i for i in pas if i.isdigit()])
    alp = len([i for i in pas if i.isalpha()])
    if not 6 <= len(pas) <= 10:
        vld = False
        print("Password must be between 6 and 10 characters")
    if not len(pas) == dgs + alp:
        vld = False
        print("Password must consist only of letters and digits")
    if not dgs >= 2:
        vld = False
        print("Password must have at least 2 digits")
    if vld:
        print("Password is valid")


password_validator(input())
