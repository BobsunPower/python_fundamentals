lines = int(input())
key = input()
lst = []
output = []
for i in range(lines):
    string = input()
    lst.append(string)
    if key in string:
        output.append(string)
print(f"{lst}\n{output}")
