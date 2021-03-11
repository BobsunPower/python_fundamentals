time_lst = list(map(int, input().split()))
mid = len(time_lst) // 2
left = 0
right = 0
for i in time_lst[:mid]:
    if i == 0:
        left *= 0.8
    else:
        left += i
for i in reversed(time_lst[mid + 1:]):
    if i == 0:
        right *= 0.8
    else:
        right += i
time = min([left, right])
if left == time:
    winner = 'left'
else:
    winner = 'right'
print(f'The winner is {winner} with total time: {time:.1f}')
