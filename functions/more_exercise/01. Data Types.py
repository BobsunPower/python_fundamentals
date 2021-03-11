def choose(tps):
    if tps == "int":
        return int(input()) * 2
    elif tps == "real":
        return f"{float(input()) * 1.5:.2f}"
    elif tps == "str_lst":
        return f"${input()}$"


tp = input()
print(choose(tp))
