def odd_and_even_sum(dgs):
    odd = [int(dgs[i]) for i in range(len(dgs)) if int(dgs[i]) % 2 == 1]
    even = [int(dgs[i])for i in range(len(dgs)) if int(dgs[i]) % 2 == 0]
    print(f"Odd sum = {sum(odd)}, Even sum = {sum(even)}")


odd_and_even_sum(input())
