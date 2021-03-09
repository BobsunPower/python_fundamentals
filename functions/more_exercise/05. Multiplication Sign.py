def sign_check(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    elif (n1 > 0 and n2 > 0 and n3 > 0) or (n1 > 0 and n2 < 0 and n3 < 0) \
            or (n1 < 0 and n2 > 0 and n3 < 0) or (n1 < 0 and n2 < 0 and n3 > 0):
        return "positive"
    else:
        return "negative"


num1, num2, num3 = int(input()), int(input()), int(input())
print(f"{sign_check(num1, num2, num3)}")
