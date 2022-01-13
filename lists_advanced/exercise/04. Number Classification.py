lst = list(map(int, input().split(", ")))
print("Positive: " + ", ".join([str(i) for i in lst if i >= 0]),
      "\nNegative: " + ", ".join([str(i) for i in lst if i < 0]),
      "\nEven: " + ", ".join([str(i) for i in lst if i % 2 == 0]),
      "\nOdd: " + ", ".join([str(i) for i in lst if i % 2 == 1]))
