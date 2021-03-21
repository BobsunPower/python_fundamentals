while True:
    wrd = input()
    if wrd == "end":
        break
    print(f"{wrd} = {wrd[::-1]}")
