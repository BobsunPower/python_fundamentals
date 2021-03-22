lst = input().split(", ")
for pas in lst:
    if 3 <= len(pas) <= 16:
        for ch in pas:
            if not (ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_"):
                break
        else:
            print(pas)
