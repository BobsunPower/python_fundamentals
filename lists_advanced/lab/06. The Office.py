emp, fac = list(map(int, input().split())), int(input())
hpy = len([i * fac for i in emp if i >= sum(emp) / len(emp)])
if hpy >= len(emp) / 2:
    print(f"Score: {hpy}/{len(emp)}. Employees are happy!")
else:
    print(f"Score: {hpy}/{len(emp)}. Employees are not happy!")
