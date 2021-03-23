# TODO
# Compile time error
txt = input()
emo = []
for i, c in enumerate(txt):
    if c == ':':
        emo.append(txt[i:i + 2])
print('\n'.join(emo))
