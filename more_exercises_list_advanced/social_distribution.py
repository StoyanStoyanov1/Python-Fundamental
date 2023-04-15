current_population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for index in range(len(current_population)):
    current_index = current_population[index]
    if current_population[index] < minimum_wealth:
        current_population[index] += (minimum_wealth - current_index)
        max_index = current_population.index(max(current_population))
        current_population[max_index] -= (minimum_wealth - current_index)

if min(current_population) >= minimum_wealth:
    print(current_population)
else:
    print("No equal distribution possible")
