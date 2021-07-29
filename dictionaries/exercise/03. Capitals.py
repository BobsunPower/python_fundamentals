dic = zip(input().split(", "), input().split(", "))
print("\n".join([f"{i} -> {j}" for i, j in list(dic)]))
