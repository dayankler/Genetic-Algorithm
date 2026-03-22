import random

# Fitness function (maximize x^2)
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0, 10) for _ in range(5)]

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    print("Generation:", generation, "Best:", population[0])

    # Crossover
    new_population = population[:2]
    while len(new_population) < 5:
        parent1, parent2 = random.sample(population[:3], 2)
        child = (parent1 + parent2) // 2
        new_population.append(child)

    # Mutation
    population = [x + random.randint(-1, 1) for x in new_population]
