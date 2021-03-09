key = int(input())
lines = int(input())
for i in range(lines):
    before = input()
    after = chr(ord(before) + key)
    print(after, end="")
