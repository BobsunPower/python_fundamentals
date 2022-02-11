for i in input().split(", "):
    if 3 <= len(i) <= 16:
        for j in i:
            if not (j.isdigit() or j.isalpha() or j == "-" or j == "_"):
                break
        else:
            print(i)
