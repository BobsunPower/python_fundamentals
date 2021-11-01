def grades(n):
    if 2 <= n < 3:
        return "Fail"
    elif 3 <= n < 3.5:
        return "Poor"
    elif 3.5 <= n < 4.5:
        return "Good"
    elif 4.5 <= n < 5.5:
        return "Very Good"
    elif 5.5 <= n <= 6:
        return "Excellent"


print(grades(float(input())))
