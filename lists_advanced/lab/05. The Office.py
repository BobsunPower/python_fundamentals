emp_lst = list(map(int, (input().split())))
fac = int(input())
hpy_lst = [i * fac for i in emp_lst]
avg = sum(hpy_lst) / len(hpy_lst)
hpy_emp = len([i for i in hpy_lst if i > avg])
if hpy_emp >= len(emp_lst) / 2:
    print(f"Score: {hpy_emp}/{len(emp_lst)}. Employees are happy!")
else:
    print(f"Score: {hpy_emp}/{len(emp_lst)}. Employees are not happy!")
