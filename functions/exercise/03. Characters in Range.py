def ascii_range(start, stop):
    output = ""
    for i in range(ord(start) + 1, ord(stop)):
        output += (chr(i))
        if not i == ord(stop) - 1:
            output += " "
    print(output)


ascii_range(input(), input())
