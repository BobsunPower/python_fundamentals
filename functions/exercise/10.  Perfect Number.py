def perfect_number(n):
    if sum([i for i in range(1, n) if n % i == 0]) == n:
        return print("We have a perfect number!")
    print("It's not so perfect.")


perfect_number(int(input()))
