def sum_digits(number):
    odd = 0
    even = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even += int(number[i])
        else:
            odd += int(number[i])
    print(f"Odd sum = {odd}, Even sum = {even}")


sum_digits(input())
