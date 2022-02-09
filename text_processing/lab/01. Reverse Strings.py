while True:
    txt = input()
    if txt == "end":
        break
    print(f"{txt} = {txt[::-1]}")
