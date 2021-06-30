def grades(num):
    if 2.00 <= num < 3.00:
        return "Fail"
    elif 3.00 <= num < 3.50:
        return "Poor"
    elif 3.50 <= num < 4.50:
        return "Good"
    elif 4.50 <= num < 5.50:
        return "Very Good"
    elif 5.50 <= num <= 6.00:
        return "Excellent"


print(grades(float(input())))
