x = float(input())
if x == 0:
    print("zero")
else:
    if abs(x) < 1:
        print("small ", end="")
    elif abs(x) > 1000000:
        print("large ", end="")
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
