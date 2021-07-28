dic, ctr = {}, 0
while True:
    cmd = input()
    if len(cmd.split(":")) < 3:
        cmd.split("_")
        for i in dic.values():
            omg = i[0].split()
            omg = omg[0]
            if omg in cmd:
                print(f"{i[1][0]} - {i[1][1]}")
        break
    std, idn, crs = cmd.split(":")
    new = [crs, [std, idn]]
    dic[ctr] = new
    ctr += 1
