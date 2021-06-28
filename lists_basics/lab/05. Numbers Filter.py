rng, lst, out = int(input()), [], []
[lst.append(int(input())) for _ in range(rng)]
cmd = input()
if cmd == "even":
    [out.append(i) if i % 2 == 0 else "" for i in lst]
elif cmd == "odd":
    [out.append(i) if i % 2 == 1 else "" for i in lst]
elif cmd == "negative":
    [out.append(i) if i < 0 else "" for i in lst]
elif cmd == "positive":
    [out.append(i) if i >= 0 else "" for i in lst]
print(out)
