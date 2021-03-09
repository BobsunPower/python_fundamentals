tgt = list(map(lambda x: int(x), input().split()))
cmd = input()
while cmd != 'End':
    comm = cmd.split()
    command = comm[0]
    idx = int(comm[1])
    pwr = int(comm[2])
    if command == 'Shoot':
        if 0 <= idx < len(tgt):
            tgt[idx] -= pwr
            if tgt[idx] <= 0:
                tgt.remove(tgt[idx])
    elif command == 'Add':
        if 0 <= idx < len(tgt):
            tgt.insert(idx, pwr)
        else:
            print("Invalid placement!")
    else:
        range_shot = pwr
        if idx + range_shot < len(tgt)-1 and idx - range_shot >= 0:
            del tgt[idx - range_shot:idx + range_shot + 1]
        else:
            print("Strike missed!")
    cmd = input()
list_to_print = [str(i) for i in tgt]
print('|'.join(list_to_print))
