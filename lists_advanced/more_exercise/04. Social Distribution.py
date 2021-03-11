def equality(pop, min_wth):
    if sum(pop) >= len(pop) * min_wth:
        possible = True
        return possible
    else:
        possible = False
        return possible


def the_richest(pop):
    richest = max(pop)
    return pop.index(richest)


def population_status(p, pop, min_wth, idx):
    if pop[p] < min_wth:
        cur_dif = min_wth - pop[p]
        pop[p] += cur_dif
        pop[idx] -= cur_dif
        return pop
    else:
        return pop


def main():
    if equality(population, min_wealth):
        for person in range(len(population)):
            population_status(person, population, min_wealth, the_richest(population))
        print(population)
    else:
        print("No equal distribution possible")


population = list(map(int, input().split(", ")))
min_wealth = int(input())
main()
