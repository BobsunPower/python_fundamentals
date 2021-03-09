balls = int(input())
best_snow = 0
best_time = 0
best_quality = 0
total = 0
for i in range(balls):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > total:
        best_snow = snow
        best_time = time
        best_quality = quality
        total = int(value)
print(f"{best_snow} : {best_time} = {total} ({best_quality})")
