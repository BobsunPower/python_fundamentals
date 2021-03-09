def loading_bar(percent):
    bar = "["
    bar += "%" * (percent // 10)
    bar += "." * ((100 - percent) // 10)
    bar += "]"
    if not percent == 100:
        print(f"{percent}% {bar}")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"{bar}")


loading_bar(int(input()))
