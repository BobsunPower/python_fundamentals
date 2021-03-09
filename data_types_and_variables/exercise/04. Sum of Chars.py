chars = int(input())
total = 0
for i in range(chars):
    char = input()
    total += ord(char)
print(f"The sum equals: {total}")
