def perfect_number_finder(number):
    divisors = 0
    for i in range(1, number):
        if number % i == 0:
            divisors += i
    if divisors == number:
        print("We have a perfect percent!")
    else:
        print("It's not so perfect.")


perfect_number_finder(int(input()))
