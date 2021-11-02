def grades(n):
    if 2 <= n < 3:
        return "Fail"
    if 3 <= n < 3.5:
        return "Poor"
    if 3.5 <= n < 4.5:
        return "Good"
    if 4.5 <= n < 5.5:
        return "Very Good"
    if 5.5 <= n <= 6:
        return "Excellent"


print(grades(float(input())))
