def loading_bar(n):
    if n < 100:
        n = n // 10
        bar = ("%" * n) + ((10 - n) * ".")
        print(f"{n * 10}% [{bar}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


loading_bar(int(input()))
