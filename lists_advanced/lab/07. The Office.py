lst, fac = list(map(int, input().split())), int(input())
hpy = len([i * fac for i in lst if i >= sum(lst) / len(lst)])
if hpy >= (len(lst) / 2):
    print(f"Score: {hpy}/{len(lst)}. Employees are happy!")
else:
    print(f"Score: {hpy}/{len(lst)}. Employees are not happy!")
