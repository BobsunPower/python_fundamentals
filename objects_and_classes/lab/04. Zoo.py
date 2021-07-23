class Zoo:
    def __init__(self, alias):
        self.name, self.animals = alias, {"mammal": [], "fish": [], "bird": []}

    def add_animals(self, sps, alias):
        self.animals[sps].append(alias)

    def get_info(self, sps):
        kind = {"mammal": "Mammals", "fish": "Fishes", "bird": "Birds"}
        return f"{kind[sps]} in {self.name}: {', '.join(self.animals[sps])}"


zoo, tot = Zoo(input()), int(input())
for i in range(tot):
    species, name = input().split()
    zoo.add_animals(species, name)
print(f"{zoo.get_info(input())}\nTotal animals: {tot}")
