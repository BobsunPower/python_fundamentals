import re
pat = r"(^|(?<=\s))[a-zA-Z\d]+[\._-]?[a-zA-Z\d]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+)+"
[print(i.group()) for i in re.finditer(pat, input())]
