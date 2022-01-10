def loading_bar(n):
    if n == 100:
        return print(f"100% Complete!\n[{'%' * 10}]")
    print(f"{n}% [{'%' * (n // 10)}{'.' * (10 - (n // 10))}]\nStill loading...")


loading_bar(int(input()))
