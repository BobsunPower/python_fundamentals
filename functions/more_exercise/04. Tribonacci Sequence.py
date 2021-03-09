def center_point(x1, y1, x2, y2):
    if sum([abs(x1), abs(y1)]) <= sum([abs(x2), abs(y2)]):
        (x, y) = int(x1), int(y1)
    else:
        (x, y) = int(x2), int(y2)
    return x, y


a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input())
print(center_point(a1, b1, a2, b2))
