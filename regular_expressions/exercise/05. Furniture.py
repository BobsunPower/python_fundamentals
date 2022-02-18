import re
tot = 0
pat = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
print("Bought furniture:")
while True:
    cmd = input()
    if cmd == "Purchase":
        break
    vld = re.fullmatch(pat, cmd)
    if vld:
        print(vld[1])
        tot += float(vld[2]) * int(vld[4])
print(f"Total money spend: {tot:.2f}")
