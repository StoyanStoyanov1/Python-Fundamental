def social_distribution(current_population, min_population):

    for index, number in enumerate(current_population):
        if number < min_population:
            max_index = current_population.index(max(current_population))
            current_population[max_index] -= (min_population - number)
            current_population[index] = min_population

    if sum(current_population) / len(current_population) >= min_population:
        return current_population
    else:
        return "No equal distribution possible"


population = list(map(int, input().split(", ")))
minimum_weather = int(input())
print(social_distribution(population, minimum_weather))