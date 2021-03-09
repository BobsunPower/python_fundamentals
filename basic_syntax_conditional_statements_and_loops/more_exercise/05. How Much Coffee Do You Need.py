coffees = 0
while True:
    task = input()
    if task == "END":
        print(coffees)
        break
    if task == "coding" or task == "dog" or task == "cat" or task == "movie":
        coffees += 1
    elif task == "CODING" or task == "DOG" or task == "CAT" or task == "MOVIE":
        coffees += 2
    if coffees > 5:
        print("You need extra sleep")
        break
