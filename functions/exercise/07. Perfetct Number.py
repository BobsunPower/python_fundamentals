def perfect_number(n):
    dvs = 0
    for i in range(1, n):
        if n % i == 0:
            dvs += i
    if dvs == n:
        print(" We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))
