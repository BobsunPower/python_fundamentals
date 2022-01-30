class Zoo:
    def __init__(self, name):
        self.name, self.dic = name, {"mammal": [], "fish": [], "bird": []}

    def add_animals(self, sps, name):
        self.dic[sps].append(name)

    def get_info(self, sps):
        dic = {"mammal": "Mammals", "fish": "Fishes", "bird": "Birds"}
        return f"{dic[sps]} in {self.name}: {', '.join(self.dic[sps])}"


zoo, tot = Zoo(input()), int(input())
for i in range(tot):
    species, animal = input().split()
    zoo.add_animals(species, animal)
print(f"{zoo.get_info(input())}\nTotal animals: {tot}")
