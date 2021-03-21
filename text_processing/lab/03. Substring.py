wrd, match, res = input(), input(), ""
while wrd in match:
    match = match.replace(wrd, "")
print(match)
