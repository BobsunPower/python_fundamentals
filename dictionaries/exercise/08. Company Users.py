out = {}
while True:
    data = input()
    if data == "End":
        break
    firm, emp = data.split(" -> ")
    if firm not in out:
        out[firm] = []
        out[firm].append(emp)
    else:
        if emp not in out[firm]:
            out[firm].append(emp)
for firm, emp in sorted(out.items(), key=lambda x: x[0], reverse=False):
    print(f"{firm}")
    print('\n'.join([f"-- {i}" for i in emp]))
